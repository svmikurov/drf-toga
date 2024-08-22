import toga


class Buttons:

    move_btn_callbacks: dict

    @property
    def btn_move_main_box(self):
        return toga.Button(
        'На главную',
        on_press=lambda _: self.move_btn_callbacks['main_box'](),
    )

    @property
    def btn_move_words_box(self):
        return toga.Button(
        'Англо-Русский словарь',
        on_press=lambda _: self.move_btn_callbacks['words_box'](),
    )

    @property
    def btn_move_create_word_box(self):
        return toga.Button(
        text='Добавить слово',
        on_press=lambda _: self.move_btn_callbacks['create_word_box'](),
    )