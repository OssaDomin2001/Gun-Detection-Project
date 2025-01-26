import random
from gui_ui import *
from PySide6.QtWidgets import QFileDialog, QMessageBox
from PySide6.QtGui import QPixmap, Qt
import sys
import cv2 as cv
import torch
from torch import nn
import timm
import torchvision.transforms as transforms

MODEL_NAME = "efficientnet_b0"


class ObjLocModel(nn.Module):
    global MODEL_NAME

    def __init__(self):
        super(ObjLocModel, self).__init__()

        self.backbone = timm.create_model(MODEL_NAME, pretrained=True, num_classes=4)

    def forward(self, images, gt_bboxes=None):
        bboxes = self.backbone(images)

        if gt_bboxes != None:
            loss = nn.MSELoss()(bboxes, gt_bboxes)
            return bboxes, loss

        return bboxes


CURRENT_MODEL = ObjLocModel()
CURRENT_IMAGE = None


def openDefaultSystemExplorerBrowserImg(ui):
    global CURRENT_IMAGE

    file_path, _ = QFileDialog.getOpenFileName(
        ui.imageBrowseButton, "Select an image file", "", "Images (*.png *.jpg *.jpeg)"
    )

    if file_path:
        ui.imagePathLine.setText(file_path)

        if file_path.endswith((".png", ".jpg", ".jpeg")):
            CURRENT_IMAGE = cv.imread(file_path)

            pixmap = QPixmap(file_path)
            pixmap = pixmap.scaled(
                600, 400, Qt.KeepAspectRatio, Qt.SmoothTransformation
            )
            ui.mainImage.setPixmap(pixmap)
            ui.mainImage.setAlignment(Qt.AlignmentFlag.AlignCenter)

            ui.provideImageLabel.setStyleSheet("color: green;")
            ui.provideImageLabel.setText("Image OK")
        else:
            ui.mainImage.clear()

            ui.provideImageLabel.setStyleSheet("color: #aa0000;")
            ui.provideImageLabel.setText(
                "Please provide a path to a valid image (.png .jpg .jpeg)"
            )

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Warning)
            msg.setWindowIcon(QIcon("icon.png"))
            msg.setText("Selected file is not an image")
            msg.setWindowTitle("Warning")
            msg.exec()


def openDefaultModelExplorerBrowse(ui):
    global CURRENT_MODEL

    file_path, _ = QFileDialog.getOpenFileName(
        ui.modelPathLine, "Select an AI model file", "", "AI models (*.pt *.pth)"
    )
    if file_path:
        if file_path.endswith((".pt", ".pth")):
            CURRENT_MODEL.load_state_dict(torch.load(file_path, map_location="cpu"))
            CURRENT_MODEL.eval()

            ui.modelPathLine.setText(file_path)

            ui.provideModelLabel.setStyleSheet("color: green;")
            ui.provideModelLabel.setText("Model OK")
        else:
            ui.modelPathLine.clear()

            ui.provideModelLabel.setStyleSheet("color: #aa0000;")
            ui.provideModelLabel.setText(
                "Please provide a path to a valid AI model file (.pt .pth)"
            )

            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Warning)
            msg.setWindowIcon(QIcon("icon.png"))
            msg.setWindowTitle("Invalid AI model file")
            msg.setText("The selected file is not a valid AI model file (.pt .pth).")
            msg.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg.exec()


def update_image(ui, image):
    height, width, channel = image.shape
    bytes_per_line = channel * width
    image = QImage(image.data, width, height, bytes_per_line, QImage.Format_BGR888)

    pixmap = QPixmap.fromImage(image)
    pixmap = pixmap.scaled(600, 400, Qt.KeepAspectRatio, Qt.SmoothTransformation)

    ui.mainImage.setPixmap(pixmap)


def detect_weapon(ui):
    global CURRENT_IMAGE
    global CURRENT_MODEL
    CURRENT_IMAGE_COPY = CURRENT_IMAGE.copy()

    CURRENT_IMAGE = cv.cvtColor(CURRENT_IMAGE, cv.COLOR_BGR2RGB)
    transform = transforms.Compose([transforms.ToTensor()])
    input_tensor = transform(CURRENT_IMAGE).unsqueeze(0)

    with torch.no_grad():
        prediction = CURRENT_MODEL(input_tensor)
        x1, y1, x2, y2 = (
            prediction[0][0].item(),
            prediction[0][1].item(),
            prediction[0][2].item(),
            prediction[0][3].item(),
        )

    print(x1, y1, x2, y2)

    image_with_bbox = draw_bbox(CURRENT_IMAGE_COPY, x1, y1, x2, y2)
    update_image(ui, image_with_bbox)

    msg = QMessageBox()
    msg.setIcon(QMessageBox.Icon.Information)
    msg.setWindowIcon(QIcon("icon.png"))
    msg.setWindowTitle("Prediction result")

    if x1 == 0 and y1 == 0 and x2 == 0 and y2 == 0:
        msg.setText("No gun detected in the image.")
    else:
        msg.setText("Gun detected in the image.")

    msg.exec()


def draw_bbox(img, x1, y1, x2, y2):
    img_copy = img.copy()
    pt1 = int(x1), int(y1)
    pt2 = int(x2), int(y2)
    img_with_bbox = cv.rectangle(img_copy, pt1, pt2, (0, 255, 0), 5)
    return img_with_bbox


if __name__ == "__main__":
    app = QApplication(sys.argv)
    Dialog = QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)

    ###

    Dialog.setWindowTitle("PBŚ AI Gun Detection")
    app_icon = QIcon("icon.png")
    Dialog.setWindowIcon(app_icon)

    ui.imageBrowseButton.clicked.connect(
        lambda: openDefaultSystemExplorerBrowserImg(ui)
    )
    ui.modelBrowseButton.clicked.connect(lambda: openDefaultModelExplorerBrowse(ui))
    ui.detectButton.clicked.connect(lambda: detect_weapon(ui))

    ###

    Dialog.show()
    sys.exit(app.exec())
