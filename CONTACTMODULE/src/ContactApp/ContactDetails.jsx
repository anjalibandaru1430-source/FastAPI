let ContactDetails=(props)=>{
    return <div>
            <h3>Contact Details</h3>
            <pre>{JSON.stringify(props)}</pre>
            <div className="card">
                <div className="card-header">
                <img src={props.selUser.picture.large} alt="" />
                </div>
                <div className="card-body">
                <ul className="list-group">
                        <li className="list-group-item">{props.selUser.name.first}</li>
                        <li className="list-group-item">{props.selUser.dob.age}</li>
                        <li className="list-group-item">{props.selUser.email}</li>
                </ul>
                </div>
            </div>
            </div>
}
export default ContactDetails;