import './Modal.css'
export default function Modal(props) {
  return (
    <div className="modal-backdrop">
        <div className="modal">
            {props.children}
            <button onClick={props.handleclose}>Close</button>
        </div>
      
    </div>
  )
}
