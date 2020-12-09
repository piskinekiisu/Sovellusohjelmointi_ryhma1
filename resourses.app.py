from flask import request
from flask_restful import Resource
from http import HTTPStatus

from models.room import room, room_list


class RoomListResource(Resource):

    def get(self):

        data = []

        for room in room_list:
            if room.is_publish is True:
                data.append(room.data)

        return {'data': data}, HTTPStatus.OK

    def post(self):
        data = request.get_json()

        recipe = Room(name=data['name'],
                        description=data['description'],
                        date=data['date'],
                        startTime=data['startTime'],
                        duration=data['duration'],)

        room_list.append(room)

        return room.data, HTTPStatus.CREATED


class RoomResource(Resource):

    def get(self, room_id):
        room = next((room for room in room_list if room.id == room_id and room.is_publish == True), None)

        if room is None:
            return {'message': 'room not found'}, HTTPStatus.NOT_FOUND

        return room.data, HTTPStatus.OK

    def put(self, room_id):
        data = room.get_json()

        room = next((reoom for room in room_list if room.id == room_id), None)

        if room is None:
            return {'message': 'room not found'}, HTTPStatus.NOT_FOUND

        room.name = data['name']
        room.description = data['description']
        room.date = data['date']
        room.startTime = data['startTime']
        room.duration = data['duration']

        return room.data, HTTPStatus.OK

    def delete(self, room_id):
        room = next((room for room in room_list if room.id == room_id), None)

        if room is None:
            return {'message': 'room not found'}, HTTPStatus.NOT_FOUND

        room_list.remove(room)

        return {}, HTTPStatus.NO_CONTENT


class RoomPublishResource(Resource):

    def put(self, room_id):
        room = next((room for room in room_list if room.id == room_id), None)

        if room is None:
            return {'message': 'room not found'}, HTTPStatus.NOT_FOUND

        room.is_publish = True

        return {}, HTTPStatus.NO_CONTENT

    def delete(self, room_id):
        room = next((room for room in room_list if room.id == room_id), None)

        if room is None:
            return {'message': 'room not found'}, HTTPStatus.NOT_FOUND

        room.is_publish = False

        return {}, HTTPStatus.NO_CONTENT
