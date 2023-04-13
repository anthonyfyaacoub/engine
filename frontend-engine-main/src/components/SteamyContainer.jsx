import React, { useState } from 'react';
import ChatbotBubble from './SteamyBubble';
import RecommendationForm from './RecommendationForm';
import styles from './ChatBotContainer.module.css';

const ChatBotContainer = () => {
  const [isFormVisible, setIsFormVisible] = useState(false);

  const handleBubbleClick = () => {
    setIsFormVisible(!isFormVisible);
  };

  return (
    <div className={styles.chatBotContainer}>
      <ChatbotBubble onClick={handleBubbleClick} />
      {isFormVisible && (
        <div className={styles.formContainer}>
          <RecommendationForm />
        </div>
      )}
    </div>
  );
};

export default ChatBotContainer;
