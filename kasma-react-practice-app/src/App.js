import './App.css';
import React, { useState } from 'react';
import Titel from './components/Title';
import Modal from './components/Modal';
import EventList from './components/EventList';

function App() {

  const [showModal, setShowModal] = useState (false);
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

  const handleClose = () => {
    setShowModal(false);
  }

  // const handleOpen = () => {
  //   setShowModal(true);
  // }

  const subTitle = "Latest Movies";

  return (
    <div className="App">
      <Titel title="Teacher Favorite Movies" subtitle={subTitle} />
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
        showEvents && <EventList info={events} delete={handleClick}/>
      }

      {/* <Modal>
          <h1>10% percent off</h1>
          <p>kasma</p>
      </Modal> */}

      {
        showModal && <Modal handleclose={handleClose}>
            <h1>Terms and Conditions</h1>
            <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Maxime fugit praesentium laudantium aspernatur quia iure obcaecati et officiis atque nisi quas non reprehenderit modi, sequi laborum totam expedita? Voluptatem, placeat?</p>
        </Modal>
      }

      {
        !showModal && (
          <div>
            <button onClick={() => setShowModal(true)}>Show Modal</button>
          </div>
        )
      }

      <Titel title="Footer" subtitle="This is a footer" />
    </div>
  );
}

export default App;
