import React from "react";
import {makeStyles} from "@material-ui/core/styles";
import './User';

const useStyles = makeStyles({
    root: {
        display: "flex",
        flex: 1,
        flexDirection: "row",
        justifyContent: "space-around",
        textAlign: "center",
    },
    user_value: {
        marginBottom: "10px",
    },
    user_block: {
        marginTop: "50px"
    },
})

const ProjectItem = ({ project }) => {
    const classes = useStyles();
    return (
        <div>
            <div className={classes.root}>
                <div className={classes.user_value}>{project.name}</div>
                <div className={classes.user_value}>
                    {project.users.map((user) => <div>{user}</div>)}</div>
            </div>

        </div>

    )
}

const ProjectList = ({ projects }) =>{
    const classes = useStyles();
    return (
        <div className={classes.user_block}>
            <div className={classes.root}>
                <h3>Project</h3>
                <h3>Members</h3>
            </div>
            {projects.map((project) => <ProjectItem project={project} />)}
        </div>
    )
}

export default ProjectList;