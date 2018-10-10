import React from 'react';
import { StyleSheet, Text, View } from 'react-native';
import { MapView } from 'expo';
import axios from 'axios';

const { manifest } = Expo.Constants;
const api = (typeof manifest.packagerOpts === `object`) && manifest.packagerOpts.dev
  ? manifest.debuggerHost.split(`:`).shift().concat(`:3000`)
  : `api.example.com`;

export default class App extends React.Component {
  componentDidMount() {
    console.log(api)
    axios.get('http://192.168.10.239:5000/status')
      .then((res) => {
        console.log(res)
        this.setState({data: res})
      })
      .catch((e) => console.log(e))
  }

  render() {
    console.log(this.state && this.state.data)
    return (
      <MapView
        style={{ flex: 1 }}
        initialRegion={{
          latitude: 48.14935,
          longitude: 17.1135,
          latitudeDelta: 0.0922,
          longitudeDelta: 0.0421,
        }}
      />
    );
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});
