import React from "react";
import Grid from "@material-ui/core/Grid";
import {makeStyles} from "@material-ui/core/styles";

const useStyles = makeStyles({
    root: {
        display: "flex",
        flex: 1,
        flexDirection: "row",
        justifyContent: "space-around",
        textAlign: "center"
    },
    user_value: {
        marginLeft: "62px"
    },
    user_block: {
        marginTop: "50px"
    },
})

const UserItem = ({user}) => {
    const classes = useStyles();
    return (
        <div className={classes.root}>
            <div className={classes.user_value}>{user.first_name}</div>
            <div className={classes.user_value}>{user.email}</div>
        </div>
    )
}

const UserList = ({users}) =>{
    const classes = useStyles();
    return (
        <div className={classes.user_block}>
            <div className={classes.root}>
                <h3>First name</h3>
                <h3>Email</h3>
            </div>
            {users.map((user) => <UserItem user={user} />)}
        </div>
    )
}

export default UserList;