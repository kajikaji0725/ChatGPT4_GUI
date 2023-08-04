import flet as ft

class QuestionComponent:
    def __init__(self, APIKey=None) -> None:
        self.APIKey = APIKey
    
    def viewQuestoinBar(self):
        
        question = ft.Ref[ft.TextField]()