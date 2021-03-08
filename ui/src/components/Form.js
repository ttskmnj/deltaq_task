import React, { useState, useEffect } from 'react'
import axios from 'axios' 
import Select from 'react-select'


const Form = () => {
    const [ csvfiles, setcsvfiles] = useState([]);
    var selectedCsvfile;
    
    useEffect(() => {
        axios
        .get('/csvfiles')
        .then(response => {
            setcsvfiles(response.data.map(csvfile=>{
                return { value: csvfile, label: csvfile}
            }))
        })
    }, [])

    const sendCsv = () =>{
        axios
        .get(`/sendcsv/${selectedCsvfile}`)
        .then(response => {
            alert(response.data)

            return response.data
        })
    }

    return (
        <div>
            <form onSubmit={sendCsv}>
                <Select 
                    options={csvfiles}
                    onChange={(selected => selectedCsvfile = selected.value)} />
                <button type="submit">send csv</button>
            </form>
        </div>
    )
}

export default Form 