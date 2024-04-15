import React from 'react';
export default function EventList(props) {
  return (
    <div>
      {props.info.map((event, index) => (
          <React.Fragment key={event.id}>
            <p>{index + 1}-{event.title}</p>
            <button onClick={() => props.delete(event.id)}>Delete</button>
          </React.Fragment>
        ))}
    </div>
  )
}
