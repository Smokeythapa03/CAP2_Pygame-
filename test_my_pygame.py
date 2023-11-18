import unittest
import pygame
import random

def test_player_movement():
    # player movement in all directions

    # Test moving up
    ballX = 120
    ballY = 490  # Initial position
    initial_position = (ballX, ballY)

    # moving the player up
    ballY -= 10  # Assuming 10 is the amount moved up

    # Assertion for the player's new position after moving up
    assert (ballX, ballY) == (initial_position[0], initial_position[1] - 10), "Player did not move up as expected"

    # Test moving down
    # moving the player down
    ballY += 10  # Assuming 10 is the amount moved down

    # Assertion for the player's new position after moving down
    assert (ballX, ballY) == (initial_position[0], initial_position[1] + 10), "Player did not move down as expected"

    # Test moving left
    # moving the player left
    ballX -= 10  # Assuming 10 is the amount moved left

    # Assertion for the player's new position after moving left
    assert (ballX, ballY) == (initial_position[0] - 10, initial_position[1]), "Player did not move left as expected"

    # Test moving right
    # moving the player right
    ballX += 10  # Assuming 10 is the amount moved right

    # Assertion for the player's new position after moving right
    assert (ballX, ballY) == (initial_position[0] + 10, initial_position[1]), "Player did not move right as expected"
def test_collision_detection():
    # Test case for collision detection scenarios
   
 #Test when ball collides with the pole
    collision_result = collision(poleX, poleY, ballX, ballY)
    assert collision_result is True, "Collision was not detected as expected"
    def test_game_over_conditions():
    # Test case for game over conditions
    assert game_over_status is True, "Game over conditions not met as expected"
    def test_highest_score_tracking():
    # Test case for highest score tracking
    assert updated_highest_score == expected_highest_score, "Highest score not updated correctly"

    # The game code
    import pygame 
import random

pygame.init()
pygame.mixer.init()

# global varibale setting required variable
width = 700
heigth = 550
screen = pygame.display.set_mode((width,heigth))
fps = 60
clock = pygame.time.Clock()

# colors setting the color
red = (255,0,0)
black = (0,0,0)


# images that are required in game
background = pygame.image.load("assets/images/background.png").convert_alpha()
base = pygame.image.load("assets/images/road.jpg").convert_alpha()
basketball = pygame.image.load("assets/images/basketball.png").convert_alpha()
pole = pygame.image.load("assets/images/pole.png").convert_alpha()
basket = pygame.image.load("assets/images/basket.png").convert_alpha()

# sounds that need to be played while playing the game
bounce = pygame.mixer.Sound("assets/sound/assets_sound_bouncing.wav")
extras_pointSound = pygame.mixer.Sound("assets/sound/assets_sound_basket.wav")

def getPoleY(baseY):
    return random.randrange(100, baseY-200)

def moving_base(baseX , baseY, base):
    screen.blit(base, (baseX,baseY))
    screen.blit(base, (baseX+width, baseY))

def collision(poleX, poleY, ballX, ballY):
    if(ballX >= poleX and ballX <= poleX+50 and ballY > poleY):
        return True
    
    elif(ballY <-10):
        return True

    return False
#setting text that needs to be displayed in the game
def ScreenText(text, color, x,y, size,style, bold=False, itallic=False):
    font = pygame.font.SysFont(style, size, bold=bold, italic=itallic)
    screen_text = font.render(text, True, color)
    screen.blit(screen_text, (x,y))

def random_basket(poleY, baseY):
    return random.randrange(poleY+100, baseY-100)

def getHighestScore():
    with open("highest score.txt","r") as f:
        return f.read()
#setting the height and the gravity
def main():
    gameOn = True
    baseX = 0
    baseY = heigth - 50
    ballX = 120
    ballY = baseY - 60
    gravity = 5
    bouncing = 20
    poleX = 400
    poleY = getPoleY(baseY)
    baseX_vel = 0
    poleX_vel = 0
    score = 0 
    speed = 0
    gameOver = False
    basketY = random_basket(poleY, baseY)
    basket_score = 0
    score = 0
    speed_accelerating = False
    gameSpeed = 0

    try:
        highestScore = int(getHighestScore())
    except:
        highestScore = 0
    

    while gameOn:
        # taking event 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameOn = False
            
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if (gameOver == False):
                        gameSpeed = 0.001
                        bouncing = 20
                        speed = 5
                        baseX_vel = int(speed)    
                        poleX_vel = int(speed) 
            
        basketX = poleX + 35
        screen.blit(background, (0,0))
        screen.blit(basket, (basketX, basketY))
        screen.blit(pole, (poleX,poleY))
        moving_base(baseX, baseY, base)
        screen.blit(basketball, (ballX,ballY))

        # bouncing the basketball while playing
        ballY -= bouncing
        bouncing -= 1
        ballY += gravity
        if(ballY > baseY-20):
            pygame.mixer.Sound.play(bounce)
            bouncing = 10

       
        # moving pole or distracting the basketball
        poleX += -poleX_vel
        if(poleX <-100):
            poleX = width + 10
            poleY = getPoleY(baseY)
        
        # moving base for the game
        baseX += -baseX_vel
        if(baseX <= -width):
            baseX = 0
        
        # collision of basketball to make it intersting
        gameOver = collision(poleX, poleY, ballX, ballY)
        if(gameOver):
            ScreenText("Game Over",red, 200,100, 60, "Arial",bold =True)
            ScreenText("Press R to Replay", red, 240, 200, 30, "Arial", bold=True)
            pygame.display.update()

            speed =0     
            bouncing =0
            gravity =0
            baseX_vel =0
            poleX_vel =0
            gameOver = True

        # Event handling for replay 
            replay = False
            while not replay:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        gameOn = False
                        replay = True
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_r:
                            replay = True
                            # Reset game variables for replay
                            baseX = 0
                            ballX = 120
                            ballY = baseY - 60
                            poleX = 400
                            poleY = getPoleY(baseY)
                            bouncing = 0
                            speed = 4
                            baseX_vel = int(speed)
                            poleX_vel = int(speed)
                            basketY = random_basket(poleY, baseY)
                            basket_score = 0
                            score = 0
                            speed_accelerating = False
                            gameSpeed = 0
                            gameOver = False

                            # Reset sounds or displaying the sound
                            pygame.mixer.Sound.stop(bounce)
                            pygame.mixer.Sound.stop(extras_pointSound)

                            # Clear the screen
                            screen.blit(background, (0, 0))
                            pygame.display.update()
  


        # ball into the basket to gain more point or score
        if(ballX+basketball.get_width() >= basketX and ballX <= basketX+basket.get_width()
        and ballY > basketY and ballY <= basketY+basket.get_height()):
            pygame.mixer.Sound.play(extras_pointSound)
            basket_score += 100

        # accelerating the speed of ball 
        speed += gameSpeed
        # speeding up score with certian speed
        score += int(speed)

        # displaying score in the display pannel while playing the game
        ScreenText(f"Score {score}",black,10, 40, size=20, style="Calibri")
        ScreenText(f"bakset score {basket_score}",black,10, 10, size=20, style="Calibri")


        # checking highest Score or keepig record of higest scorer in a saprate text file
        if(highestScore < score):
            highestScore = score
        with open("highest score.txt","w") as f:
            f.write(str(highestScore))
        
        ScreenText(f"Highest score {highestScore}",red,width-200, 10, size=14, style="Calibri")
        
        pygame.display.update()  
        clock.tick(fps)

        
if __name__ == "__main__":
    main()
#End of coding for the basketball game
#Now you can run inorder to feel exicting moment of the selfmade game

class TestBasketballGame(unittest.TestCase):

    def setUp(self):
        pygame.init()
        self.screen = pygame.display.set_mode((700, 550))
        pygame.mixer.init()
        self.clock = pygame.time.Clock()
        # Initialize any game state or variables needed for testing
        # ...

    def tearDown(self):
        pygame.quit()
        # Clean up after each test
        # ...

    def test_player_movement(self):
        # Test player movement
        ballY = 490  # Initial ball position
        gravity = 5

        # Simulate movement events (e.g., left, right, up, down)
        # Use Pygame to simulate player movement
        # Assert the expected outcomes for each movement
        keys = {pygame.K_LEFT: (-5, 0), pygame.K_RIGHT: (5, 0), pygame.K_UP: (0, -5), pygame.K_DOWN: (0, 5)}
        for key, movement in keys.items():
            pygame.event.post(pygame.event.Event(pygame.KEYDOWN, {'key': key}))
            ballY += movement[1]  # Adjust the ball position based on simulated movement
            ballY += gravity  # Apply gravity

            # Assert the expected outcomes for each movement
            self.assertTrue(ballY >= 0)  # Ensure ball stays within screen boundaries, or any other relevant assertions

    def test_collision_detection(self):
        # Test collision detection
        ballX = 400  # Initial ball position
        ballY = 300
        poleX = 350  # Initial pole position
        poleY = 250
        baseY = 550
        speed = 5
        gravity = 5

        # Simulate collision events between objects
        # Assert the expected outcomes for collisions
        ballY -= speed  # Move ball up (simulate jump)
        ballY += gravity  # Apply gravity

        # Check collision between ball and pole
        collision = ballX >= poleX and ballX <= poleX + 50 and ballY > poleY
        self.assertTrue(collision)

        # Check collision with base (game over condition)
        collision_base = ballY >= baseY
        self.assertTrue(collision_base)

    def test_scoring_mechanism(self):
        # Test scoring mechanism
        ballX = 350  # Ball position near the basket
        ballY = 400
        basketX = 350
        basketY = 300
        basket_score = 0

        # Simulate scoring events (e.g., scoring a basket)
        # Assert the expected outcomes for scoring
        ballX = basketX + 20  # Ball enters the basket
        ballY = basketY + 10

        if ballX >= basketX and ballX <= basketX + 50 and ballY >= basketY and ballY <= basketY + 50:
            basket_score += 100  # Increment score for scoring a basket
        self.assertEqual(basket_score, 100)

    

if __name__ == '__main__':
    unittest.main()

