import React from "react";
import Grid from '@material-ui/core/Grid';
import Paper from '@material-ui/core/Paper';
import { makeStyles } from '@material-ui/core/styles';
import {Grow} from "@material-ui/core";

const useStyles = makeStyles((theme) => ({
    root: {
        margin: "auto",
    },
    paper: {
        padding: theme.spacing(3),
        textAlign: "center",
        color: theme.palette.text.secondary,
    },
}));

const AuthorItem = ({author}) => {
    const style = useStyles()
    return (
        <tr>
            <td className={style.paper}>
                {author.first_name}
            </td>
            <td className={style.paper}>
                {author.last_name}
            </td>
            <td className={style.paper}>
                {author.birthday_year}
            </td>
        </tr>
    )
}


const AuthorList = ({authors}) => {
    const style = useStyles()
    return (
        <table className={style.root}>
            <th>
                First name
            </th>
            <th>
                Last Name
            </th>
            <th>
                Birthday year
            </th>
            {authors.map((author) => <AuthorItem author={author} />)}
        </table>
   )
}


export default AuthorList