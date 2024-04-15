export default function Titel (props) {
    return (
        <>
            <h1 className="title">{props.title}</h1>
            <br />
            <p className="subTitle">{props.subtitle}</p>
        </>
    )
}