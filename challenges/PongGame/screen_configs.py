"""Pong court size and configurations."""
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

# Automatic changes if screen width or height are modified
TOP_BORDER = (SCREEN_HEIGHT / 2) - 10
BOTTOM_BORDER = -TOP_BORDER
RIGHT_BORDER = (SCREEN_WIDTH / 2) - 10
LEFT_BORDER = -RIGHT_BORDER

# Positions for right and left scores on the screen
right_score_position = (SCREEN_WIDTH * 0.15, SCREEN_HEIGHT * 0.25)
left_score_position = (SCREEN_WIDTH * -0.15, SCREEN_HEIGHT * 0.25)
