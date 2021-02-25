import random
from game import constants
from game.action import Action
from game.point import Point

class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    """

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        ball = cast["ball"][0] # There's only one ball
        brick = cast["brick"] # there's multiple bricks
        paddle = cast["paddle"][0] #  there's only one paddle

        #  check if the ball hits the paddle
        for i in range(11):
            x = paddle._position.get_x()
            y = paddle._position.get_y()
            position = Point(x+i, y)
            if ball.get_position().equals(position):
                v = random.randint(-2,2)
                v_y = ball._velocity.get_y()
                velocity = Point(v,v_y*-1)
                ball.set_velocity(velocity)

        #  Check if the brick is hit and remove it
        for i in brick:
            if ball.get_position().equals(i.get_position()):
                brick.remove(i)
                v = random.randint(-2,2)
                v_y = ball._velocity.get_y()
                velocity = Point(v,v_y*-1)
                ball.set_velocity(velocity)

        #  check if the ball hits the bottom of the screen
        # if ball._position.get_y() == 20:
        #     position = Point(0,0)
        #     ball.set_position(position)
        #     velocity = Point(0,0)
        #     ball.sett_velocity(velocity)
