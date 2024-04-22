import './Title.css' 
export default function Titel (props) {
    return (
        <div className='title-block'>
            <h1 className="title">{props.title}</h1>
            <br />
            <p className="subTitle">{props.subtitle}</p>
        </div>
    )
}