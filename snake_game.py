import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Constants
WINDOW_WIDTH = 640
WINDOW_HEIGHT = 480
GRID_SIZE = 20
GRID_WIDTH = WINDOW_WIDTH // GRID_SIZE
GRID_HEIGHT = WINDOW_HEIGHT // GRID_SIZE
FPS = 10

# Colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
DARK_GREEN = (0, 200, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
GRAY = (40, 40, 40)

# Directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)


class Snake:
    def __init__(self):
        self.reset()

    def reset(self):
        self.body = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.grow = False

    def move(self):
        head_x, head_y = self.body[0]
        dir_x, dir_y = self.direction
        new_head = ((head_x + dir_x) % GRID_WIDTH, (head_y + dir_y) % GRID_HEIGHT)

        # Check self collision
        if new_head in self.body:
            return False

        self.body.insert(0, new_head)
        if not self.grow:
            self.body.pop()
        else:
            self.grow = False
        return True

    def change_direction(self, new_direction):
        # Prevent 180-degree turns
        opposite = (-self.direction[0], -self.direction[1])
        if new_direction != opposite:
            self.direction = new_direction

    def grow_snake(self):
        self.grow = True

    def draw(self, screen):
        for i, segment in enumerate(self.body):
            color = GREEN if i == 0 else DARK_GREEN
            rect = pygame.Rect(segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE - 1, GRID_SIZE - 1)
            pygame.draw.rect(screen, color, rect)


class Food:
    def __init__(self):
        self.position = (0, 0)
        self.randomize()

    def randomize(self, snake_body=None):
        while True:
            pos = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
            if snake_body is None or pos not in snake_body:
                self.position = pos
                break

    def draw(self, screen):
        rect = pygame.Rect(self.position[0] * GRID_SIZE, self.position[1] * GRID_SIZE, GRID_SIZE - 1, GRID_SIZE - 1)
        pygame.draw.rect(screen, RED, rect)


def draw_grid(screen):
    for x in range(0, WINDOW_WIDTH, GRID_SIZE):
        pygame.draw.line(screen, GRAY, (x, 0), (x, WINDOW_HEIGHT))
    for y in range(0, WINDOW_HEIGHT, GRID_SIZE):
        pygame.draw.line(screen, GRAY, (0, y), (WINDOW_WIDTH, y))


def draw_text(screen, text, size, color, x, y, center=True):
    font = pygame.font.Font(None, size)
    surface = font.render(text, True, color)
    rect = surface.get_rect()
    if center:
        rect.center = (x, y)
    else:
        rect.topleft = (x, y)
    screen.blit(surface, rect)


def main():
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Snake Game")
    clock = pygame.time.Clock()

    snake = Snake()
    food = Food()
    score = 0
    game_over = False
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if game_over:
                    if event.key == pygame.K_SPACE:
                        snake.reset()
                        food.randomize()
                        score = 0
                        game_over = False
                    elif event.key == pygame.K_ESCAPE:
                        running = False
                else:
                    if event.key == pygame.K_UP:
                        snake.change_direction(UP)
                    elif event.key == pygame.K_DOWN:
                        snake.change_direction(DOWN)
                    elif event.key == pygame.K_LEFT:
                        snake.change_direction(LEFT)
                    elif event.key == pygame.K_RIGHT:
                        snake.change_direction(RIGHT)

        if not game_over:
            # Move snake
            alive = snake.move()
            if not alive:
                game_over = True

            # Check if snake ate food
            if snake.body[0] == food.position:
                snake.grow_snake()
                score += 10
                food.randomize(snake.body)

        # Draw everything
        screen.fill(BLACK)
        draw_grid(screen)
        food.draw(screen)
        snake.draw(screen)

        # Draw score
        draw_text(screen, f"Score: {score}", 36, WHITE, 60, 20, center=False)

        if game_over:
            # Draw game over overlay
            overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
            overlay.set_alpha(200)
            overlay.fill(BLACK)
            screen.blit(overlay, (0, 0))
            draw_text(screen, "GAME OVER", 72, RED, WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 50)
            draw_text(screen, f"Final Score: {score}", 48, WHITE, WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 20)
            draw_text(screen, "Press SPACE to play again", 36, WHITE, WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 80)
            draw_text(screen, "Press ESC to quit", 36, WHITE, WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 120)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
