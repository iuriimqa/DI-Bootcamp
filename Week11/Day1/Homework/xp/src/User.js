import "./User.css"
import "./Exercise4.css"

const UserFavoriteColors = (props) => {
    console.log("props", props);
    const { userinfo } = props
    return (
        <div>
            <h1>hello {userinfo.firstName}</h1>
            <ul>{userinfo.favAnimals.map((item) =>
                <li>{item}</li>
            )}</ul>
        </div>
    )
}

const Exercise4 = () => {
    const style_header = {
        color: "white",
        backgroundColor: "DodgerBlue",
        padding: "10px",
        fontFamily: "Arial"
    };
    return (
        <>
            <h1 className="title" style={style_header}>Some Element</h1>
            <p className="para">This is a paragraph</p>
            <a href="#">This is a link</a>
            <h3>This is the form:</h3>
            <form>
                <label>Enter your name</label>
                <input type="text"></input><button type="submit">Submit</button>
            </form>
            <h3>This is the Image:</h3>
            <img src="https://res.klook.com/image/upload/fl_lossy.progressive,q_65/c_fill,w_480,h_384/cities/liw377az16sxmp9a6ylg.webp" />
            <ul>
                <li>Coffee</li>
                <li>Tea</li>
                <li>Milk</li>
            </ul>


        </>
    )
}

export { UserFavoriteColors, Exercise4 }