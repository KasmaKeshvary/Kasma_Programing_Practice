import './App.css';
import { useState } from 'react';
function App() {

  // let name = "Mahdi";
  const [name , setName] = useState ("Mahdi");
  const [events , setEvents] = useState ([
    {title: "Thor: Love And Thunder (2022)", id: 1},
    {title: "The Gray Man (2022)", id: 2},
    {title: "The Sea Beast (2022)", id: 3},
    {title: "Top Gun Maverick (2022)", id: 4},
    {title: "Doctor Strange in Multiverse of Madness (2022)", id: 5},
    {title: "Hustle (2022)", id: 6}
  ]);

  const handleClick = () => {
    
    setName("Kasma");
    console.log(name);
    // console.log(setName);
  }

  return (
    <div className="App">
      <h1>{name}</h1>
      <button onClick={handleClick}>Change Name</button>
      {
        events.map((event, index) => (
          <div key={event.id}>
            <p>{index + 1}-{event.title}</p>
          </div>
        ))
      }
    </div>
  );
}

export default App;
