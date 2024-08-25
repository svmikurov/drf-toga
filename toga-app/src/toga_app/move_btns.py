"""Module with buttons for moving between boxes."""

from toga import Button

from toga_app.boxes.styled import (
    HALF_SMALL_PADDING,
    StyledButton,
)


class BoxButtons(StyledButton):
    """Buttons for moving between boxes."""

    move_btn_callbacks: dict

    def __init__(self, move_btn_callbacks: dict) -> None:
        """Add button callback function."""
        super().__init__()
        self.move_btn_callbacks = move_btn_callbacks

    @property
    def btn_move_main_box(self) -> Button:
        """Go to Main window."""
        return StyledButton(
            'На главную',
            on_press=lambda _: self.move_btn_callbacks['main_box'](),
            padding_right=HALF_SMALL_PADDING,
        )

    @property
    def btn_move_words_box(self) -> Button:
        """Go to Word List window."""
        return StyledButton(
            'Словарь',
            on_press=lambda _: self.move_btn_callbacks['words_box'](),
            padding_left=HALF_SMALL_PADDING,
        )

    @property
    def btn_move_create_word_box(self) -> Button:
        """Go to Create Word window."""
        return StyledButton(
            'Добавить слово',
            on_press=lambda _: self.move_btn_callbacks['create_word_box'](),
            padding_left=HALF_SMALL_PADDING,
        )

    @property
    def btn_move_update_word_box(self) -> Button:
        """Go to Update Word window."""
        return StyledButton(
            'Изменить слово',
            on_press=lambda _: self.move_btn_callbacks['update_word_box'](),
            padding_right=HALF_SMALL_PADDING,
        )

    @property
    def btn_move_explore_lsp_box(self) -> Button:
        """Go to Update Word window."""
        return StyledButton(
            'Эксперимент с LSP',
            on_press=lambda _: self.move_btn_callbacks['explore_lsp_box'](),
        )

    @property
    def btn_move_auth_box(self) -> Button:
        """Go to Auth Box."""
        return StyledButton(
            'Войти',
            on_press=lambda _: self.move_btn_callbacks['auth_box'](),
        )
