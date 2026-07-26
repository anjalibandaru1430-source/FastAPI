let ContactList = (props)=>{
    let SelContactHandler=(user)=>{
        //console.log(user.name.first)
        props.getSelContact(user);
    }
    return <div>
                <h2>ContactList Comp</h2>
                <pre>{JSON.stringify(props)}</pre>
                <table className="table">
                    <thead className="bg-dark">
                    <tr>
                        <th>User Id</th>
                        <th>Name</th>
                        <th>City</th>
                        <th>Email</th>
                    </tr>
                    </thead>
                    <tbody>
                    {
                        props.users.map((user,index)=>{
                            return <tr key={index} onMouseOver={SelContactHandler.bind(null,user)}>
                                        <td>{user.login.uuid.substring(32)}</td>
                                        <td>{user.name.first}</td>
                                        <td>{user.location.city}</td>
                                        <td>{user.email}</td>
                                    </tr>
                        })
                    }
                    </tbody>
                </table>
            </div>
}
export default ContactList;