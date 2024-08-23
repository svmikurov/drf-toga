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
        'Словарь',
        on_press=lambda _: self.move_btn_callbacks['words_box'](),
    )

    @property
    def btn_move_create_word_box(self):
        return StyledButton(
        'Добавить слово',
        on_press=lambda _: self.move_btn_callbacks['create_word_box'](),
    )

    @property
    def btn_move_update_word_box(self):
        return StyledButton(
        'Изменить слово',
        on_press=lambda _: self.move_btn_callbacks['update_word_box'](),
    )
