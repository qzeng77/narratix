from huggingface_hub import InferenceClient
from src.config.settings import LLM_CONFIG
from src.utils.logger import logger
from typing import Dict, List

class DialogueManager:
    def __init__(self):
        # Initialize HuggingFace Inference Client
        self.client = InferenceClient(
            provider="together",
            api_key=LLM_CONFIG["api_key"]
        )
        self.model_name = LLM_CONFIG["model_name"]
        
        # Initialize conversation history
        self.conversation_history: List[Dict[str, str]] = []
        
        # Define system prompt
        self.system_prompt = """You are an experienced Game Master in a fantasy RPG setting. 
        Your role is to create an engaging and immersive experience for the player while 
        maintaining consistency in the story and world."""
    
    def format_history(self) -> str:
        """Format conversation history into a string"""
        if not self.conversation_history:
            return ""
            
        history_str = []
        for entry in self.conversation_history[-5:]:  # Only use last 5 interactions
            history_str.append(f"Player: {entry['player']}")
            history_str.append(f"Game Master: {entry['game_master']}")
        
        return "\n".join(history_str)
    
    def process_input(self, user_input: str, game_state: str = None) -> str:
        """Process player input and generate Game Master's response"""
        try:
            logger.info(f"Processing user input: {user_input}")
            
            # Build the complete prompt
            history = self.format_history()
            context = f"\nCurrent game state:\n{game_state}" if game_state else ""
            
            # Create messages for chat
            messages = [
                {
                    "role": "system",
                    "content": self.system_prompt
                }
            ]
            
            # Add context and history if they exist
            if context or history:
                messages.append({
                    "role": "user",
                    "content": f"{context}\n\n{history}"
                })
                messages.append({
                    "role": "assistant",
                    "content": "I understand the current state and history. How can I help?"
                })
            
            # Add current user input
            messages.append({
                "role": "user",
                "content": user_input
            })
            
            # Get response from the model
            response = self.client.chat.completions.create(
                model=self.model_name,
                messages=messages,
                max_tokens=LLM_CONFIG["max_new_tokens"],
                temperature=LLM_CONFIG["temperature"],
                # top_k=LLM_CONFIG.get("top_k", 50),
                # top_p=LLM_CONFIG.get("top_p", 0.9),
            )
            
            logger.info(f"Generated response: {response}")

            # Extract the content from the response
            content = response.choices[0].message["content"].strip()
            
            # Update conversation history
            self.conversation_history.append({
                "player": user_input,
                "game_master": content
            })
            
            return content
            
        except Exception as e:
            logger.error(f"Error in dialogue processing: {e}")
            return "I apologize, but I'm having trouble processing that. Could you please try again?"
    
    def get_conversation_history(self) -> List[Dict[str, str]]:
        """Return the current conversation history"""
        return self.conversation_history
    
    def clear_history(self):
        """Clear the conversation history"""
        self.conversation_history = []