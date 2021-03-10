import React from 'react';
import {BottomNavigation, BottomNavigationAction} from "@material-ui/core";
import {makeStyles} from "@material-ui/core/styles";
import MenuIcon from "@material-ui/icons/Menu";
import RestoreIcon from '@material-ui/icons/Restore';
import FavoriteIcon from '@material-ui/icons/Favorite';
import LocationOnIcon from '@material-ui/icons/LocationOn';
import FolderIcon from '@material-ui/icons/Folder'

const useStyles = makeStyles({
    root: {
        flexGrow: 1,
        position: "fixed",
        left: 0,
        bottom: 0,
        width: "100%"
    },
})

function Footer() {
    const classes = useStyles();
    const [value, setValue] = React.useState("recents")
    const handleChange = (event, newValue) => {
        setValue(newValue);
    };
    return (
        <BottomNavigation
            value={value}
            onChange={handleChange}
            className={classes.root}>

                <BottomNavigationAction
                    label="Recents"
                    value="recents"
                    icon={<RestoreIcon />}
                />
                <BottomNavigationAction
                    label="Favourites"
                    value="favourites"
                    icon={<FavoriteIcon />}
                />
                <BottomNavigationAction
                    label="Nearby"
                    value="nearby"
                    icon={<LocationOnIcon />}
                />
                <BottomNavigationAction
                    label="Folder"
                    value="folder"
                    icon={<FolderIcon />}
                />
        </BottomNavigation>
    )
}
export default Footer;