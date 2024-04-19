import pyautogui
import tkinter as tk


def move_and_click(x, y):
    pyautogui.moveTo(x, y)
    pyautogui.click()