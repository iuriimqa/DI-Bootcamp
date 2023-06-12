const User = (props) => {
    console.log(props);
    const {userinfo} = props;
    const {id,name,email,username} = userinfo;
    return <>
        <img src={`https://robohash.org/${id}?size=150x150`} />
        <h2>{name}</h2>
        <p>{username}</p>
        <p>{email}</p>
    </>;
}

export default User