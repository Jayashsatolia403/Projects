import React from 'react'

import StartGame from './StartGame'


export default class PlayClass extends React.Component {
    state = {
        loading: true,
        rooms: [],
        roomId: "",
        decidedRoom: {}
    }

    async componentDidMount() {
        const url = `http://127.0.0.1:8000/play/`
        const response = await fetch(url)
        if (response.ok) {
            const data = await response.json();
            this.setState({rooms: data, loading:false})
        }
        else{
            console.log("Error")
        }
    }

    handleChange = (e) => {
        const {id , value} = e.target   
        this.setState(prevState => ({
            ...prevState,
            [id] : value
        }))
    }

    joinRoom(givenRoom) {
        this.setState({decidedRoom: givenRoom})
        const url = `http://127.0.0.1:8000/play/${givenRoom.roomId}/joinRoom/`
        fetch(url, {
            headers: {
                "Content-type": "application/json",
                "Authorization": "Token 900e748b0ad69b5d233b15c5483873395d572fe8"
            }
        }).then(res => {return res.json()}).then(data => console.log(data)).catch(error => console.log("Error"))
    }

    availabeRooms() {
        const url = "http://127.0.0.1:8000/play/"
        fetch(url, {
            headers: {
                "Content-type": "application/json",
                "Authorization": "Token ec5e0e255e66fe1a9378325c7edc3c02a3ed4709"
            }
        }).then(res => {return res.json()}).then(data => this.setState({rooms: data})).catch(error => console.log("Error"))
    }

    createRoom() {
        console.log(this.state.roomId)
        const information = {
            "roomId": this.state.roomId
        }

        fetch("http://127.0.0.1:8000/play/createRoom/", {
            method: 'POST', 
            body: JSON.stringify(information),
            headers: {
                "Content-type": "application/json",
                "Authorization": "Token ec5e0e255e66fe1a9378325c7edc3c02a3ed4709"
            }
        }).then(res => {
            return res.json()
            })
            .then(data => console.log(data))
            .catch(error => console.log("Error"))
    }

    handleSubmitClick = (e) => {
        e.preventDefault();
        this.createRoom()
    }

    render() {
        if (this.state.loading) {
            return <h1>Loading</h1>
        }

        console.log(this.state.decidedRoom)

        if (Object.keys(this.state.decidedRoom).length != 0) {
            return <StartGame room={this.state.decidedRoom} />
        }

        return (
            <>
                <div className="card col-12 col-lg-4 login-card mt-2 hv-center">
                    <h1>Welcome to Game Room!</h1>
    
                    <h2>You can join or create Room Here!</h2>
    
                    <form>
                        <div className="form-group text-left">
                            <label>RoomId</label>
                            <input type="text" 
                                className="form-control" 
                                id="roomId" 
                                placeholder="Enter Room Id"
                                onChange={this.handleChange} 
                            />
                        </div>
                        <h1>    </h1>
                        <div>
                            <button type="submit" onClick={this.handleSubmitClick}>Create Room</button>
                        </div>
                    </form>
    
                    <div>
                        <h1>Available Rooms</h1>
                    </div>    
    
                    <div>
                        <h1>RoomID - RoomName - NoOfPlayers</h1>
                        {this.state.rooms.map(room => (
                            <div key={room.id}>
                                <h2>{room.id} - {room.roomId} - {room.noOfPlayers}</h2>
                                <button onClick={e=> this.joinRoom(room)}>Join</button>
                            </div>
                        ))}
                    </div>
                </div>
            </>
        )
    }
}