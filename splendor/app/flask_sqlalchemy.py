import typing as t

from flask_sqlalchemy import SQLAlchemy

from splendor.app.flask import app


db = SQLAlchemy(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


@app.before_first_request
def create_database(*args, **kwargs):
    app.logger.info('Creating database...')
    db.create_all()


@app.teardown_request
def shutdown_session(*args, **kwargs):
    app.logger.info('Shutting down database session...')
    db.session.remove()


# Below codes are implemented only for typing perpose.
# these won't be available on runtime.
if t.TYPE_CHECKING:
    # Typing hints for Flask-SQLAlchemy
    from flask_sqlalchemy import BaseQuery
    from flask_sqlalchemy import Model
    from flask_sqlalchemy import SQLAlchemy
    from sqlalchemy.orm.scoping import scoped_session as session

    class db(SQLAlchemy):
        from sqlalchemy import create_engine, create_mock_engine, engine_from_config, inspect, BLANK_SCHEMA, CheckConstraint, Column, ColumnDefault, Computed, Constraint, DDL, DefaultClause, FetchedValue, ForeignKey, ForeignKeyConstraint, Identity, Index, MetaData, PrimaryKeyConstraint, Sequence, Table, ThreadLocalMetaData, UniqueConstraint, alias, all_, and_, any_, asc, between, bindparam, case, cast, collate, column, delete, desc, distinct, except_, except_all, exists, extract, false, func, funcfilter, insert, intersect, intersect_all, join, LABEL_STYLE_DEFAULT, LABEL_STYLE_DISAMBIGUATE_ONLY, LABEL_STYLE_NONE, LABEL_STYLE_TABLENAME_PLUS_COL, lambda_stmt, lateral, literal, literal_column, modifier, not_, null, nulls_first, nulls_last, nullsfirst, nullslast, or_, outerjoin, outparam, over, select, subquery, table, tablesample, text, true, tuple_, type_coerce, union, union_all, update, values, within_group, ARRAY, BIGINT, BigInteger, BINARY, BLOB, BOOLEAN, Boolean, CHAR, CLOB, DATE, Date, DATETIME, DateTime, DECIMAL, Enum, FLOAT, Float, INT, INTEGER, Integer, Interval, JSON, LargeBinary, NCHAR, NUMERIC, Numeric, NVARCHAR, PickleType, REAL, SMALLINT, SmallInteger, String, TEXT, Text, TIME, Time, TIMESTAMP, TypeDecorator, Unicode, UnicodeText, VARBINARY, VARCHAR
        from sqlalchemy.orm import AliasOption, AppenderQuery, AttributeEvent, AttributeEvents, AttributeState, Bundle, CascadeOptions, ClassManager, ColumnProperty, CompositeProperty, DeclarativeMeta, EXT_CONTINUE, EXT_SKIP, EXT_STOP, FromStatement, IdentityMap, InspectionAttr, InspectionAttrInfo, InstanceEvents, InstanceState, InstrumentationEvents, InstrumentedAttribute, Load, LoaderCriteriaOption, MANYTOMANY, MANYTOONE, Mapped, Mapper, MapperEvents, MapperProperty, NOT_EXTENSION, ONETOMANY, ORMExecuteState, PropComparator, Query, QueryContext, QueryEvents, QueryableAttribute, RelationshipProperty, Session, SessionEvents, SessionTransaction, SynonymProperty, UOWTransaction, UserDefinedOption, aliased, as_declarative, backref, class_mapper, clear_mappers, close_all_sessions, column_property, composite, configure_mappers, contains_alias, contains_eager, create_session, declarative_base, declarative_mixin, declared_attr, defaultload, defer, deferred, dynamic_loader, eagerload, foreign, has_inherited_table, immediateload, join, joinedload, lazyload, load_only, make_transient, make_transient_to_detached, mapper, merge_frozen_result, merge_result, noload, object_mapper, object_session, outerjoin, polymorphic_union, public_factory, query_expression, raiseload, reconstructor, registry, relation, relationship, remote, scoped_session, selectin_polymorphic, selectinload, sessionmaker, subqueryload, synonym, synonym_for, undefer, undefer_group, validates, was_deleted, with_expression, with_loader_criteria, with_parent, with_polymorphic

        class Model(Model):
            __tablename__: str
            __bind_key__: t.Optional[str]
            query: BaseQuery

        session: session
