"""Move buttons."""

from toga import Button

from toga_app.boxes.styled import StyledButton


class MoveBoxButtons:
    """Move buttons."""

    move_btn_callbacks: dict

    def __init__(self, move_btn_callbacks: dict) -> None:
        """Add button callback function."""
        self.move_btn_callbacks = move_btn_callbacks

    @property
    def btn_move_main_box(self) -> Button:
        """Go to Main window."""
        return StyledButton(
            'На главную',
            on_press=lambda _: self.move_btn_callbacks['main_box'](),
        )

    @property
    def btn_move_words_box(self) -> Button:
        """Go to Word List window."""
        return StyledButton(
            'Словарь',
            on_press=lambda _: self.move_btn_callbacks['words_box'](),
        )

    @property
    def btn_move_create_word_box(self) -> Button:
        """Go to Create Word window."""
        return StyledButton(
            'Добавить слово',
            on_press=lambda _: self.move_btn_callbacks['create_word_box'](),
        )

    @property
    def btn_move_update_word_box(self) -> Button:
        """Go to Update Word window."""
        return StyledButton(
            'Изменить слово',
            on_press=lambda _: self.move_btn_callbacks['update_word_box'](),
        )
