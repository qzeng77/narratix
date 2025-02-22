# tests/test_dialogue.py

import pytest
from unittest.mock import patch, MagicMock
from src.game.dialogue_manager import DialogueManager

@pytest.fixture
def mock_llm():
    """Create a mock LLM for testing"""
    with patch('src.game.dialogue_manager.InferenceClient', new_callable=MagicMock) as mock:
        yield mock

def test_dialogue_manager_initialization(mock_llm):
    """Test initialization of DialogueManager"""
    dialogue_manager = DialogueManager()
    assert dialogue_manager is not None

def test_process_input_success(mock_llm):
    """Test successful processing of input"""
    dialogue_manager = DialogueManager()
    mock_response = MagicMock()
    mock_response.choices = [MagicMock(message={"content": "Mock response"})]
    mock_llm.return_value.chat.completions.create.return_value = mock_response
    
    response = dialogue_manager.process_input("Test input")
    assert response == "Mock response"

def test_process_input_error(mock_llm):
    """Test processing of input with error"""
    dialogue_manager = DialogueManager()
    mock_llm.return_value.chat.completions.create.side_effect = Exception("Mock error")
    
    response = dialogue_manager.process_input("Test input")
    assert response == "I apologize, but I'm having trouble processing that. Could you please try again?"

def test_conversation_history(mock_llm):
    """Test conversation history management"""
    dialogue_manager = DialogueManager()
    mock_response = MagicMock()
    mock_response.choices = [MagicMock(message={"content": "Mock response"})]
    mock_llm.return_value.chat.completions.create.return_value = mock_response
    
    dialogue_manager.process_input("Test input")
    history = dialogue_manager.get_conversation_history()
    assert len(history) > 0
    dialogue_manager.clear_history()
    history = dialogue_manager.get_conversation_history()
    assert len(history) == 0