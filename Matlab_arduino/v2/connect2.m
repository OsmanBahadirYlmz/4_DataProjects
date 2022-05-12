function varargout = connect2(varargin)
% CONNECT2 MATLAB code for connect2.fig
%      CONNECT2, by itself, creates a new CONNECT2 or raises the existing
%      singleton*.
%
%      H = CONNECT2 returns the handle to a new CONNECT2 or the handle to
%      the existing singleton*.
%
%      CONNECT2('CALLBACK',hObject,eventData,handles,...) calls the local
%      function named CALLBACK in CONNECT2.M with the given input arguments.
%
%      CONNECT2('Property','Value',...) creates a new CONNECT2 or raises the
%      existing singleton*.  Starting from the left, property value pairs are
%      applied to the GUI before connect2_OpeningFcn gets called.  An
%      unrecognized property name or invalid value makes property application
%      stop.  All inputs are passed to connect2_OpeningFcn via varargin.
%
%      *See GUI Options on GUIDE's Tools menu.  Choose "GUI allows only one
%      instance to run (singleton)".
%
% See also: GUIDE, GUIDATA, GUIHANDLES

% Edit the above text to modify the response to help connect2

% Last Modified by GUIDE v2.5 25-Jan-2022 01:47:44

% Begin initialization code - DO NOT EDIT
gui_Singleton = 1;
gui_State = struct('gui_Name',       mfilename, ...
                   'gui_Singleton',  gui_Singleton, ...
                   'gui_OpeningFcn', @connect2_OpeningFcn, ...
                   'gui_OutputFcn',  @connect2_OutputFcn, ...
                   'gui_LayoutFcn',  [] , ...
                   'gui_Callback',   []);
if nargin && ischar(varargin{1})
    gui_State.gui_Callback = str2func(varargin{1});
end

if nargout
    [varargout{1:nargout}] = gui_mainfcn(gui_State, varargin{:});
else
    gui_mainfcn(gui_State, varargin{:});
end
% End initialization code - DO NOT EDIT


% --- Executes just before connect2 is made visible.
function connect2_OpeningFcn(hObject, eventdata, handles, varargin)
% This function has no output args, see OutputFcn.
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
% varargin   command line arguments to connect2 (see VARARGIN)

% Choose default command line output for connect2
handles.output = hObject;

% Update handles structure
guidata(hObject, handles);

% UIWAIT makes connect2 wait for user response (see UIRESUME)
% uiwait(handles.figure1);
 

% --- Outputs from this function are returned to the command line.
function varargout = connect2_OutputFcn(hObject, eventdata, handles) 
% varargout  cell array for returning output args (see VARARGOUT);
% hObject    handle to figure
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Get default command line output from handles structure
varargout{1} = handles.output;
clear
clear all
clc
disp("1")
global a
 a = arduino("COM7",'uno');
configurePin(a,'D3','DigitalOutput')

% --- Executes on button press in ledon.
function ledon_Callback(hObject, eventdata, handles)
% hObject    handle to ledon (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
global a
writeDigitalPin(a,'D3',1);

% --- Executes on button press in ledoff.
function ledoff_Callback(hObject, eventdata, handles)
% hObject    handle to ledoff (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
global a
writeDigitalPin(a,'D3',0);


% --- Executes on button press in close.
function close_Callback(hObject, eventdata, handles)
% hObject    handle to close (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
global a
fclose(a);
 delete(a);


% --- Executes on button press in drivemotor.
function drivemotor_Callback(hObject, eventdata, handles)
% hObject    handle to drivemotor (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
global a
ePin1 = str2double(get(handles.rpm,'String'));
writePWMVoltage(a,'D5',ePin1);
writeDigitalPin(a,'D6',1);
writeDigitalPin(a,'D7',0);

set(handles.disprpm, 'string', num2str(ePin1))

% --- Executes on button press in stopmotor.
function stopmotor_Callback(hObject, eventdata, handles)
% hObject    handle to stopmotor (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)
global a
writePWMVoltage(a,'D5',0);
writeDigitalPin(a,'D6',0);
writeDigitalPin(a,'D7',0);



function rpm_Callback(hObject, eventdata, handles)
% hObject    handle to rpm (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of rpm as text
%        str2double(get(hObject,'String')) returns contents of rpm as a double


% --- Executes during object creation, after setting all properties.
function rpm_CreateFcn(hObject, eventdata, handles)
% hObject    handle to rpm (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end



function disprpm_Callback(hObject, eventdata, handles)
% hObject    handle to disprpm (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    structure with handles and user data (see GUIDATA)

% Hints: get(hObject,'String') returns contents of disprpm as text
%        str2double(get(hObject,'String')) returns contents of disprpm as a double


% --- Executes during object creation, after setting all properties.
function disprpm_CreateFcn(hObject, eventdata, handles)
% hObject    handle to disprpm (see GCBO)
% eventdata  reserved - to be defined in a future version of MATLAB
% handles    empty - handles not created until after all CreateFcns called

% Hint: edit controls usually have a white background on Windows.
%       See ISPC and COMPUTER.
if ispc && isequal(get(hObject,'BackgroundColor'), get(0,'defaultUicontrolBackgroundColor'))
    set(hObject,'BackgroundColor','white');
end
