import React, { useState, useEffect, useRef } from "react";
import axios from "axios";
import "./App.css"; // Import styles

const ChatBot = () => {
  const [userMessage, setUserMessage] = useState("");
  const [chatHistory, setChatHistory] = useState([]);
  const chatContainerRef = useRef(null);

  // Scroll to the bottom of the chat when new messages are added
  useEffect(() => {
    if (chatContainerRef.current) {
      chatContainerRef.current.scrollTop =
        chatContainerRef.current.scrollHeight;
    }
  }, [chatHistory]);

  // Function to handle user input and API request
  const handleSendMessage = async () => {
    if (!userMessage.trim()) return; // Prevent empty messages

    // Add user's message to chat
    setChatHistory((prev) => [
      ...prev,
      { sender: "user", message: userMessage },
    ]);

    try {
      // Send message to Flask backend
      const response = await axios.post("http://127.0.0.1:5000/chat", {
        message: userMessage,
      });

      // Add chatbot response to chat
      setChatHistory((prev) => [
        ...prev,
        { sender: "bot", message: response.data.response },
      ]);

      // Clear the input field
      setUserMessage("");
    } catch (error) {
      console.error("Error:", error);
      setChatHistory((prev) => [
        ...prev,
        { sender: "bot", message: "Sorry, I couldn't connect to the server." },
      ]);
    }

    // Clear input field
    setUserMessage("");
  };

  return (
    <div className="chat-container">
      <h1>Relationship Chatbot</h1>
      <div classname="chat-box" ref={chatContainerRef}>
        {chatHistory.map((chat, index) => (
          <div key={index} className={`message ${chat.sender}`}>
            <p>{chat.message}</p>
          </div>
        ))}
      </div>

      <div className="input-container">
        <input
          type="text"
          value={userMessage}
          onChange={(e) => setUserMessage(e.target.value)}
          placeholder="Type your message..."
        />
        <button onClick={handleSendMessage}>Send</button>
      </div>
    </div>
  );
};

export default ChatBot;
