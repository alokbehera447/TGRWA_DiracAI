import { ReactElement } from "react";
import { Props } from "./interfaces";
/**
 * Usage: https://github.com/samhirtarif/react-audio-recorder#audiorecorder-component
 *
 *
 * @prop `onRecordingComplete` Method that gets called when save recording option is clicked
 * @prop `recorderControls` Externally initilize hook and pass the returned object to this param, this gives your control over the component from outside the component.
 * https://github.com/samhirtarif/react-audio-recorder#combine-the-useaudiorecorder-hook-and-the-audiorecorder-component
 * @prop `classes` Is an object with attributes representing classes for different parts of the component
 */
declare const AudioRecorder: (props: Props) => ReactElement;
export default AudioRecorder;
