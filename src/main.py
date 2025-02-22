# src/main.py

from src.game.dialogue_manager import DialogueManager
from src.models.game_state import GameState, Character
from src.utils.logger import logger

class GameMaster:
    def __init__(self):
        self.dialogue_manager = DialogueManager()
        self.game_state = None
    
    def start_new_game(self, player_name: str, character_class: str):
        """Initialize a new game with player character"""
        logger.info(f"Starting new game with character: {player_name} ({character_class})")
        player = Character(name=player_name, character_class=character_class)
        self.game_state = GameState(player=player)
        
        # Generate introduction
        intro = self.dialogue_manager.process_input(
            f"I am {player_name}, a {character_class} starting my adventure. "
            "Please introduce me to this world."
        )
        return intro
    
    def process_turn(self, player_input: str) -> str:
        """Process a single game turn"""
        if not self.game_state:
            return "Please start a new game first."
        
        # Add current game state context to the input
        context = self.game_state.get_state_summary()
        
        # Process the input and return response
        return self.dialogue_manager.process_input(player_input, context)

def main():
    """Main function for testing"""
    game_master = GameMaster()
    
    print("Welcome to AI RPG Game Master!")
    print("Starting new game...")
    
    intro = game_master.start_new_game("Aldric", "Warrior")
    print("\nGame Master:", intro)
    
    # Test simple interaction
    while True:
        user_input = input("\nYour action (or 'quit' to exit): ")
        if user_input.lower() == 'quit':
            break
            
        response = game_master.process_turn(user_input)
        print("\nGame Master:", response)

    dialogue_manager = DialogueManager()
    print("Dialogue Manager initialized successfully.")

if __name__ == "__main__":
    main()