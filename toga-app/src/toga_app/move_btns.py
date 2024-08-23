from toga_app.boxes.styled import StyledButton

class Buttons:

    move_btn_callbacks: dict

    def __init__(self, move_btn_callbacks):
        self.move_btn_callbacks = move_btn_callbacks

    @property
    def btn_move_main_box(self):
        return StyledButton(
        'На главную',
        on_press=lambda _: self.move_btn_callbacks['main_box'](),
    )

    @property
    def btn_move_words_box(self):
        return StyledButton(
        'Англо-Русский словарь',
        on_press=lambda _: self.move_btn_callbacks['words_box'](),
    )

    @property
    def btn_move_create_word_box(self):
        return StyledButton(
        'Добавить слово',
        on_press=lambda _: self.move_btn_callbacks['create_word_box'](),
    )