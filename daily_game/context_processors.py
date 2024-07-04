import datetime
from datetime import date
from .utils import generate_game
from daily_game.models import Daily_Game

def get_game_context(request):

  """
  Try to retrieve a game for today's date.  If one has not been generated
  call the generate_game function to generate the game.
  The generated game data is used in all three rounds of the games, and only called 
  in the template.
  """

  try:
      date_today = datetime.date.today()
      this_game = Daily_Game.objects.get(date = date_today)
      game_id = this_game.id
      my_letters = this_game.letters   
      my_numbers = this_game.numbers
      target   = this_game.num_target
      conundrum  = this_game.conundrum 

  except Daily_Game.DoesNotExist:
      my_letters, my_numbers, target, conundrum = generate_game()
      daily_game_obj = Daily_Game.objects.create(letters=my_letters, numbers=my_numbers, num_target=target, conundrum=conundrum)
      daily_game_obj.save()

  game_context = { 'my_letters' : my_letters ,  'my_numbers': my_numbers, 'target': target, 'conundrum': conundrum }

  return game_context