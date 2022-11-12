import React, {useState} from "react";
import Button from 'react-bootstrap/Button';
import "../styles/Country.css"
import PropTypes from "prop-types";

function Country(props) {
    const [selected, changeSelected] = useState(false);

    return (
    <tr className={selected ? "selected-country" : ""}>
        <td>{props.name}</td>
        <td>{props.capital}</td>
        <td>
           { selected ? 
           <Button variant="danger" onClick={() => changeSelected(false)}>Remove</Button> : 
           <Button variant="success" onClick={() => changeSelected(true)}>Add</Button>}
        </td>
    </tr>)
}

Country.propTypes = {
    country: PropTypes.object
};

Country.defaultProps = {
    capital: "Not Available"
}

export default Country;