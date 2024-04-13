import './App.css';
import { useState } from 'react';
function App() {

  const [showEvents, setShowEvents] = useState (true);
  const [events, setEvents] = useState ([
    {title: "Thor: Love And Thunder (2022)", id: 1},
    {title: "The Gray Man (2022)", id: 2},
    {title: "The Sea Beast (2022)", id: 3},
    {title: "Top Gun Maverick (2022)", id: 4},
    {title: "Doctor Strange in Multiverse of Madness (2022)", id: 5},
    {title: "Hustle (2022)", id: 6}
  ]);

  const handleClick = (id) => {
    setEvents((prevEvents) => {
      return prevEvents.filter((event) => {
        return id !== event.id;
      })
    })
  }

  return (
    <div className="App">
      
      {
        showEvents && (
          <div>
            <button onClick={() => setShowEvents(false)}>Hide</button>
          </div>
        )
      }

      {
        !showEvents && (
          <div>
            <button onClick={() => setShowEvents(true)}>Show</button>
          </div>
        )
      }

      {
        showEvents && events.map((event, index) => (
          <div key={event.id}>
            <p>{index + 1}-{event.title}</p>
            <button onClick={() => handleClick(event.id)}>Delete</button>
          </div>
        ))
      }
    </div>
  );
}

export default App;
