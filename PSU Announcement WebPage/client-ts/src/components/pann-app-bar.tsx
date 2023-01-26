import { AppBar, Divider, Drawer, Grid, IconButton, List, ListItem, ListItemButton, ListItemIcon, ListItemText, Menu, MenuItem, Toolbar, Typography } from "@mui/material";
import { Menu as MenuIcon, AccountCircle, ChevronLeft, Home, Campaign } from "@mui/icons-material";
import { useState } from "react";
import { useAppCtx } from "../AppProvider";
import { useNavigate } from "react-router-dom";
import "./pann-app-bar.css";


function PannAppBar() {
  const { userInfo, action } = useAppCtx()
  const [anchorEl, setAnchorEl] = useState(null);
  const [anchorNav, setAnchorNav] = useState(false);
  const navigate = useNavigate();

  const handleOpenMenu = (event: any) => {
    setAnchorEl(event.currentTarget);
  };

  const handleCloseMenu = () => {
    setAnchorEl(null);
  };

  return (
    <AppBar position="static" style={{ backgroundColor: '#3f51b5' }}>
      <Drawer
        anchor="left"
        open={anchorNav}
        onClose={() => setAnchorNav(false)}
      >
        <div className="drawer-header">
          <IconButton onClick={() => setAnchorNav(false)}>
            <ChevronLeft style={{ fontSize: '40px' }}/>
          </IconButton>
        </div>
        <Divider />
        <List>
          <ListItem>
            <ListItemButton onClick={() => navigate("/home")}>
              <Grid container direction="column" alignItems="center">
                <Grid item>
                  <ListItemIcon>
                    <Home style={{ fontSize: '100px' }}/>
                  </ListItemIcon>
                </Grid>
                <Grid item className="text">
                  <ListItemText primary={<div>Home</div>} />
                </Grid>
              </Grid>
            </ListItemButton>
          </ListItem>
            <ListItem>
              <ListItemButton onClick={() => navigate("/announcement")}>
                <Grid container direction="column" alignItems="center">
                  <Grid item>
                    <ListItemIcon>
                      <Campaign style={{ fontSize: '100px' }}/>
                    </ListItemIcon>
                  </Grid>
                  <Grid item className="text">
                    <ListItemText primary={<div>Announcement</div>} />
                  </Grid>
                </Grid>
              </ListItemButton>
            </ListItem>
        </List>
      </Drawer>
      <Toolbar>
        <div className="toolbar-left">
          <IconButton
            size="large"
            edge="start"
            color="inherit"
            aria-label="menu"
            onClick={() => setAnchorNav(true)}
          >
            <MenuIcon style={{ fontSize: '40px' }}/>
          </IconButton>
        </div>
        <Typography variant="h6" component="div" className="toolbar-title" style={{ color: '#fff', flexGrow: 1 }}>
          PSU Announcement
        </Typography>
        <div className="toolbar-right" style={{display: 'flex', alignItems: 'center'}}>
          <Typography variant="h6" component="div" className="toolbar-username" style={{ color: '#fff', padding: '0px 10px', marginRight: '10px'}}>
            {userInfo.displayName}
          </Typography>
          <IconButton
            size="large"
            aria-label="account of current user"
            aria-controls="menu-appbar"
            aria-haspopup="true"
            onClick={handleOpenMenu}
            color="inherit"
          >
            <AccountCircle style={{ fontSize: '40px' }}/>
          </IconButton>
          <Menu
              id="menu-appbar"
              anchorEl={anchorEl}
              anchorOrigin={{
                  vertical: 'bottom',
                  horizontal: 'right',
              }}
              keepMounted
              transformOrigin={{
                  vertical: 'top',
                  horizontal: 'right',
              }}
              open={Boolean(anchorEl)}
              onClose={handleCloseMenu}
          >
              {userInfo.ready && <MenuItem onClick={() => void action.signOut()}>Log out</MenuItem>}
          </Menu>
        </div>
      </Toolbar>
    </AppBar>
  );
}

export default PannAppBar; 