import flet as ft

class ViewComponent:
    def __init__(self, questionComponent, talkingComponent) -> None:
        self.questionComponent = questionComponent
        self.talkingComponent = talkingComponent
    