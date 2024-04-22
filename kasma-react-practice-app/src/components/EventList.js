import React from 'react';
import styles from './EventList.module.css'

export default function EventList(props) {
  return (
    <div>
      {props.info.map((event, index) => (
          <div className={styles.card} key={event.id}>
            <p>{index + 1}-{event.title}</p>
            <button id={styles.butt}  onClick={() => props.delete(event.id)}>Delete</button>
          </div>
        ))}
    </div>
  )
}
