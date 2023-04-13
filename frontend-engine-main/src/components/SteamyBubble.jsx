import React from 'react';
import styles from './ChatbotBubble.module.css';

const ChatbotBubble = ({ onClick }) => {
  return (
    <div className={styles.chatbotBubbleContainer} onClick={onClick}>
      <div className={styles.chatbotBubble}>
        <img src="./steamy.jpg" alt="Chat" />
      </div>
    </div>
  );
};

export default ChatbotBubble;
