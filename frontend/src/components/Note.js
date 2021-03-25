import React from "react";
import {makeStyles} from "@material-ui/core/styles";

const useStyles = makeStyles({
    root: {
        display: "flex",
        flex: 1,
        flexDirection: "row",
        justifyContent: "space-around",
        textAlign: "center"
    },
    user_block: {
        marginTop: "50px"
    },
})

const NoteItem = ({ note }) => {
    const classes = useStyles();
    return (
        <div className={classes.root}>
            <div>{note.project}</div>
            <div>{note.text}</div>
            <div>{note.creator}</div>
        </div>
    )
}

const NoteList = ({ notes }) =>{
    const classes = useStyles();
    return (
        <div className={classes.user_block}>
            <div className={classes.root}>
                <h3>Project</h3>
                <h3>Text</h3>
                <h3>Creator</h3>
            </div>
            {notes.map((note) => <NoteItem note={note} />)}
        </div>
    )
}

export default NoteList;