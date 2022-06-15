from marshmallow import Schema, fields


class DirectorSchema(Schema):
	id = fields.Int(dump_only=True)
	name = fields.Str()


class GenreSchema(Schema):
	id = fields.Int(dump_only=True)
	name = fields.Str()


class MoviesSchema(Schema):
	id = fields.Int(dump_only=True)
	title = fields.Str()
	description = fields.Str()
	trailer = fields.Str()
	year = fields.Int()
	rating = fields.Float()
	genre = fields.Nested(GenreSchema)
	director = fields.Nested(DirectorSchema)
