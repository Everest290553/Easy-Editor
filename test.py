from PyQt5 import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
import os
from PIL import Image, ImageFilter
import sys

app = QApplication([])

window = QWidget()
window.setWindowTitle('Easy Editor')
window.resize(625,400)

folder_btn = QPushButton(window)
folder_btn.setText('Folder')
folder_btn.resize(120,30)
folder_btn.move(0,0)

exit_btn = QPushButton(window)
exit_btn.setText('Exit')
exit_btn.resize(120,30)
exit_btn.move(0,0)
exit_btn.hide()

image_list = QListWidget(window)
image_list.resize(110,360)
image_list.move(7,30)

image_label = QLabel(window)
image_label.setText('image')
image_label.hide()
image_label.resize(500,350)
image_label.move(120, 0)

left_btn = QPushButton(window)
left_btn.resize(110,30)
left_btn.setText('Left')
left_btn.move(115, 365)

right_btn = QPushButton(window)
right_btn.resize(110,30)
right_btn.setText('Right')
right_btn.move(215, 365)

mirror_btn = QPushButton(window)
mirror_btn.resize(110,30)
mirror_btn.setText('Mirror')
mirror_btn.move(315, 365)

focus_btn = QPushButton(window)
focus_btn.resize(110,30)
focus_btn.setText('Focus')
focus_btn.move(415, 365)

white_black_btn = QPushButton(window)
white_black_btn.resize(110,30)
white_black_btn.setText('W/B')
white_black_btn.move(515, 365)

actions = 0

def filter(files, extensions):
    global result
    result = []
    for filename in files:
        for ext in extensions:
            if filename.endswith(ext):
                result.append(filename)
    return result
def chooseWorkdir():
    global workdir
    workdir = QFileDialog.getExistingDirectory()
def open_folder():
    extensions = ['.jpg', '.jpeg', '.png' , '.gif', '.bmp']
    chooseWorkdir()
    global files
    try:
        files = filter(os.listdir(workdir), extensions)
        image_list.clear()
        image_list.addItems(files)
        folder_btn.hide()
        exit_btn.show()
    except:
        not_found = QMessageBox()
        not_found.setText('Folder not found!')
        not_found.exec_()
def showChosenImage():
    global chosen_image
    global path
    chosen_image = image_list.selectedItems()[0].text()
    path = workdir+'/'+chosen_image
    pixmap_image = QPixmap(path)
    pixmap_image = pixmap_image.scaled(image_label.width(), image_label.height())
    image_label.setPixmap(pixmap_image)
    image_label.show()
def turn_left():
    global actions
    try:
        with Image.open(path) as image:
            new_image = image.transpose(Image.ROTATE_90)
            if actions == 0:
                new_image.save('new.png')
                actions += 1
                print(actions)
            else:
                text, ok = QInputDialog.getText(window, 'Image choice', 'Type "Original" if you want to make changes to the original image\nType "Continue" if you want to make changes to already changed image.')
                if ok and text == '':
                    not_creating = QMessageBox()
                    not_creating.setText('You did not write anything!')
                    not_creating.exec_()
                elif ok and text == 'Original':
                    new_image1 = image.transpose(Image.ROTATE_90)
                    new_image1.save('new.png')
                elif ok and text == 'Continue':
                    with Image.open('new.png') as image_1:
                        new_image2 = image_1.transpose(Image.ROTATE_90)
                        new_image2.save('new.png')
                else:
                    not_ = QMessageBox()
                    not_.setText('You did not write what you needed!')
                    not_.exec_()
        pixmap = QPixmap('new.png')
        pixmap = pixmap.scaled(image_label.width(), image_label.height())
        image_label.setPixmap(pixmap)
    except NameError:
        not_found = QMessageBox()
        not_found.setText('You did not choose an image!')
        not_found.exec_()
def turn_right():
    global actions
    try:
        with Image.open(path) as image:
            new_image = image.transpose(Image.ROTATE_270)
            if actions == 0:
                new_image.save('new.png')
                actions += 1
                print(actions)
            else:
                text, ok = QInputDialog.getText(window, 'Image choice', 'Type "Original" if you want to make changes to the original image\nType "Continue" if you want to make changes to already changed image.')
                if ok and text == '':
                    not_creating = QMessageBox()
                    not_creating.setText('You did not write anything!')
                    not_creating.exec_()
                elif ok and text == 'Original':
                    new_image1 = image.transpose(Image.ROTATE_270)
                    new_image1.save('new.png')
                elif ok and text == 'Continue':
                    with Image.open('new.png') as image_1:
                        new_image2 = image_1.transpose(Image.ROTATE_270)
                        new_image2.save('new.png')
                else:
                    not_ = QMessageBox()
                    not_.setText('You did not write what you needed!')
                    not_.exec_()
        pixmap = QPixmap('new.png')
        pixmap = pixmap.scaled(image_label.width(), image_label.height())
        image_label.setPixmap(pixmap)
    except NameError:
        not_found = QMessageBox()
        not_found.setText('You did not choose an image!')
        not_found.exec_()
def mirror():
    global actions
    try:
        with Image.open(path) as image:
            new_image = image.transpose(Image.FLIP_LEFT_RIGHT)
            if actions == 0:
                new_image.save('new.png')
                actions += 1
                print(actions)
            else:
                text, ok = QInputDialog.getText(window, 'Image choice', 'Type "Original" if you want to make changes to the original image\nType "Continue" if you want to make changes to already changed image.')
                if ok and text == '':
                    not_creating = QMessageBox()
                    not_creating.setText('You did not write anything!')
                    not_creating.exec_()
                elif ok and text == 'Original':
                    new_image1 = image.transpose(Image.FLIP_LEFT_RIGHT)
                    new_image1.save('new.png')
                elif ok and text == 'Continue':
                    with Image.open('new.png') as image_1:
                        new_image2 = image_1.transpose(Image.FLIP_LEFT_RIGHT)
                        new_image2.save('new.png')
                else:
                    not_ = QMessageBox()
                    not_.setText('You did not write what you needed!')
                    not_.exec_()
        pixmap = QPixmap('new.png')
        pixmap = pixmap.scaled(image_label.width(), image_label.height())
        image_label.setPixmap(pixmap)
    except NameError:
        not_found = QMessageBox()
        not_found.setText('You did not choose an image!')
        not_found.exec_()
def focus():
    global actions
    try:
        with Image.open(path) as image:
            new_image = image.filter(ImageFilter.BLUR)
            if actions == 0:
                new_image.save('new.png')
                actions += 1
                print(actions)
            else:
                text, ok = QInputDialog.getText(window, 'Image choice', 'Type "Original" if you want to make changes to the original image\nType "Continue" if you want to make changes to already changed image.')
                if ok and text == '':
                    not_creating = QMessageBox()
                    not_creating.setText('You did not write anything!')
                    not_creating.exec_()
                elif ok and text == 'Original':
                    new_image1 = image.filter(ImageFilter.BLUR)
                    new_image1.save('new.png')
                elif ok and text == 'Continue':
                    with Image.open('new.png') as image_1:
                        new_image2 = image_1.filter(ImageFilter.BLUR)
                        new_image2.save('new.png')
                else:
                    not_ = QMessageBox()
                    not_.setText('You did not write what you needed!')
                    not_.exec_()
        pixmap = QPixmap('new.png')
        pixmap = pixmap.scaled(image_label.width(), image_label.height())
        image_label.setPixmap(pixmap)
    except NameError:
        not_found = QMessageBox()
        not_found.setText('You did not choose an image!')
        not_found.exec_()
def white_black():
    global actions
    try:
        with Image.open(path) as image:
            new_image = image.convert('L')
            if actions == 0:
                new_image.save('new.png')
                actions += 1
                print(actions)
            else:
                text, ok = QInputDialog.getText(window, 'Image choice', 'Type "Original" if you want to make changes to the original image\nType "Continue" if you want to make changes to already changed image.')
                if ok and text == '':
                    not_creating = QMessageBox()
                    not_creating.setText('You did not write anything!')
                    not_creating.exec_()
                elif ok and text == 'Original':
                    new_image1 = image.convert('L')
                    new_image1.save('new.png')
                elif ok and text == 'Continue':
                    with Image.open('new.png') as image_1:
                        new_image2 = image_1.convert('L')
                        new_image2.save('new.png')
                else:
                    not_ = QMessageBox()
                    not_.setText('You did not write what you needed!')
                    not_.exec_()
        pixmap = QPixmap('new.png')
        pixmap = pixmap.scaled(image_label.width(), image_label.height())
        image_label.setPixmap(pixmap)
    except NameError:
        not_found = QMessageBox()
        not_found.setText('You did not choose an image!')
        not_found.exec_()
def exit_():
    sys.exit()

folder_btn.clicked.connect(open_folder)
image_list.itemClicked.connect(showChosenImage)
left_btn.clicked.connect(turn_left)
right_btn.clicked.connect(turn_right)
mirror_btn.clicked.connect(mirror)
focus_btn.clicked.connect(focus)
white_black_btn.clicked.connect(white_black)
exit_btn.clicked.connect(exit_)

window.show()
app.exec_()