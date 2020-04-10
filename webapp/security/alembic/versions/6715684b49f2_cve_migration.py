"""“cve_migration”

Revision ID: 6715684b49f2
Revises: e8760725610a
Create Date: 2020-04-08 11:06:29.210002

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "6715684b49f2"
down_revision = "e8760725610a"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "bug",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("uri", sa.String(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "cve_reference",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("uri", sa.String(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "cve_bugs",
        sa.Column("cve_id", sa.String(), nullable=True),
        sa.Column("bug_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(["bug_id"], ["bug.id"],),
        sa.ForeignKeyConstraint(["cve_id"], ["cve.id"],),
    )
    op.create_table(
        "cve_references",
        sa.Column("cve_id", sa.String(), nullable=True),
        sa.Column("cve_reference_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(["cve_id"], ["cve.id"],),
        sa.ForeignKeyConstraint(["cve_reference_id"], ["cve_reference.id"],),
    )
    op.add_column("cve", sa.Column("approved_by", sa.String(), nullable=True))
    op.add_column("cve", sa.Column("assigned_to", sa.String(), nullable=True))
    op.add_column("cve", sa.Column("component", sa.String(), nullable=True))
    op.add_column("cve", sa.Column("crd", sa.String(), nullable=True))
    op.add_column("cve", sa.Column("cvss", sa.String(), nullable=True))
    op.add_column("cve", sa.Column("description", sa.String(), nullable=True))
    op.add_column(
        "cve", sa.Column("discovered_by", sa.String(), nullable=True)
    )
    op.add_column(
        "cve", sa.Column("last_updated_date", sa.String(), nullable=True)
    )
    op.add_column("cve", sa.Column("mitigation", sa.String(), nullable=True))
    op.add_column("cve", sa.Column("notes", sa.String(), nullable=True))
    op.add_column("cve", sa.Column("packages", sa.JSON(), nullable=True))
    op.add_column("cve", sa.Column("priority", sa.String(), nullable=True))
    op.add_column("cve", sa.Column("public_date", sa.String(), nullable=True))
    op.add_column(
        "cve", sa.Column("public_date_usn", sa.String(), nullable=True)
    )
    op.add_column("cve", sa.Column("status", sa.String(), nullable=True))
    op.add_column(
        "cve", sa.Column("ubuntu_description", sa.String(), nullable=True)
    )
    op.add_column(
        "release", sa.Column("component", sa.String(), nullable=True)
    )
    op.add_column(
        "release", sa.Column("development", sa.Boolean(), nullable=True)
    )
    op.add_column("release", sa.Column("esm", sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("release", "esm")
    op.drop_column("release", "development")
    op.drop_column("release", "component")
    op.drop_column("cve", "ubuntu_description")
    op.drop_column("cve", "status")
    op.drop_column("cve", "public_date_usn")
    op.drop_column("cve", "public_date")
    op.drop_column("cve", "priority")
    op.drop_column("cve", "packages")
    op.drop_column("cve", "notes")
    op.drop_column("cve", "mitigation")
    op.drop_column("cve", "last_updated_date")
    op.drop_column("cve", "discovered_by")
    op.drop_column("cve", "description")
    op.drop_column("cve", "cvss")
    op.drop_column("cve", "crd")
    op.drop_column("cve", "component")
    op.drop_column("cve", "assigned_to")
    op.drop_column("cve", "approved_by")
    op.drop_table("cve_references")
    op.drop_table("cve_bugs")
    op.drop_table("cve_reference")
    op.drop_table("bug")
    # ### end Alembic commands ###