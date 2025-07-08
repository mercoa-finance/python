# Reference
## EntityGroup
<details><summary><code>client.entity_group.<a href="src/mercoa/entity_group/client.py">get_all</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all entity groups. If using a JWT, will return all groups the entity is part of. If using an API key, will return all groups for the organization.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity_group.get_all()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The maximum number of results to return. Defaults to 1. Max is 10.
    
</dd>
</dl>

<dl>
<dd>

**starting_after:** `typing.Optional[EntityGroupId]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity_group.<a href="src/mercoa/entity_group/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create an entity group
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa
from mercoa.entity_group_types import EntityGroupCreateRequest

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity_group.create(
    request=EntityGroupCreateRequest(
        foreign_id="your-group-id",
        name="Coastal Corporation",
        email_to_name="coastalcorp",
        entity_ids=[
            "ent_e8c2af94-61cd-4036-a765-80341209167b",
            "ent_1176dd0c-12e1-41c7-85a5-ae9b4746e64b",
            "ent_3dbb4ede-2d1d-49be-a996-a5dfad3641be",
        ],
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `EntityGroupCreateRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity_group.<a href="src/mercoa/entity_group/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get an entity group
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity_group.get(
    entity_group_id="entg_a3582b70-fd04-4888-9185-a640ae9048be",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_group_id:** `EntityGroupId` — Entity Group ID or Entity Group ForeignID
    
</dd>
</dl>

<dl>
<dd>

**return_entity_metadata:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Return simple key/value metadata for the specified keys for the entities in the group. For more complex metadata, use the Metadata API.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity_group.<a href="src/mercoa/entity_group/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update an entity group
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa
from mercoa.entity_group_types import EntityGroupUpdateRequest

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity_group.update(
    entity_group_id="entg_a3582b70-fd04-4888-9185-a640ae9048be",
    request=EntityGroupUpdateRequest(
        foreign_id="your-group-id",
        name="AcmeConglomerate",
        email_to_name="acmegroup",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_group_id:** `EntityGroupId` — Entity Group ID or Entity Group ForeignID
    
</dd>
</dl>

<dl>
<dd>

**request:** `EntityGroupUpdateRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity_group.<a href="src/mercoa/entity_group/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete an entity group
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity_group.delete(
    entity_group_id="entityGroupId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_group_id:** `EntityGroupId` — Entity Group ID or Entity Group ForeignID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity_group.<a href="src/mercoa/entity_group/client.py">get_token</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generate a JWT token for an entity group with the given options. This token can be used to authenticate to any entity in the entity group in the Mercoa API and iFrame.

<Warning>We recommend using [this endpoint](/api-reference/entity-group/user/get-token). This will enable features such as approvals and comments.</Warning>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa
from mercoa.entity_types import TokenGenerationOptions

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity_group.get_token(
    entity_group_id="entg_a0f6ea94-0761-4a5e-a416-3c453cb7eced",
    request=TokenGenerationOptions(
        expires_in="1h",
        session_id="session_123",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_group_id:** `EntityGroupId` — Entity Group ID or Entity Group ForeignID
    
</dd>
</dl>

<dl>
<dd>

**request:** `TokenGenerationOptions` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity_group.<a href="src/mercoa/entity_group/client.py">add_entities</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add entities to an entity group
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa
from mercoa.entity_group_types import EntityGroupAddEntitiesRequest

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity_group.add_entities(
    entity_group_id="entg_a0f6ea94-0761-4a5e-a416-3c453cb7eced",
    request=EntityGroupAddEntitiesRequest(
        entity_ids=[
            "ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
            "ent_21661ac1-a2a8-4465-a6c0-64474ba8181d",
        ],
        copy_users_from="ent_1176dd0c-12e1-41c7-85a5-ae9b4746e64b",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_group_id:** `EntityGroupId` — Entity Group ID or Entity Group ForeignID
    
</dd>
</dl>

<dl>
<dd>

**request:** `EntityGroupAddEntitiesRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity_group.<a href="src/mercoa/entity_group/client.py">remove_entities</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Remove entities from an entity group
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa
from mercoa.entity_group_types import EntityGroupRemoveEntitiesRequest

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity_group.remove_entities(
    entity_group_id="entg_a0f6ea94-0761-4a5e-a416-3c453cb7eced",
    request=EntityGroupRemoveEntitiesRequest(
        entity_ids=[
            "ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
            "ent_21661ac1-a2a8-4465-a6c0-64474ba8181d",
        ],
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_group_id:** `EntityGroupId` — Entity Group ID or Entity Group ForeignID
    
</dd>
</dl>

<dl>
<dd>

**request:** `EntityGroupRemoveEntitiesRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## EntityGroup User
<details><summary><code>client.entity_group.user.<a href="src/mercoa/entity_group/user/client.py">find</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Search entity group users
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity_group.user.find(
    entity_group_id="entg_8545a84e-a45f-41bf-bdf1-33b42a55812c",
    name="John",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_group_id:** `EntityGroupId` — Entity Group ID or Entity Group ForeignID
    
</dd>
</dl>

<dl>
<dd>

**foreign_id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — ID used to identify user in your system
    
</dd>
</dl>

<dl>
<dd>

**role:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filter users by role. If multiple roles are provided, users with any of the roles will be returned.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Filter users by name. Partial matches are supported.
    
</dd>
</dl>

<dl>
<dd>

**email:** `typing.Optional[str]` — Filter users by email. Partial matches are supported.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of entities to return. Limit can range between 1 and 100, and the default is 10.
    
</dd>
</dl>

<dl>
<dd>

**starting_after:** `typing.Optional[EntityUserId]` — The ID of the user to start after. If not provided, the first page of entities will be returned.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity_group.user.<a href="src/mercoa/entity_group/user/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create entity user that will be added to all entities in the group. If a user with the same foreignId already exists, the user will be updated with the new information.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa
from mercoa.entity_group_types import (
    EntityGroupUserEntityRequest,
    EntityGroupUserRequest,
)

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity_group.user.create(
    entity_group_id="entg_8545a84e-a45f-41bf-bdf1-33b42a55812c",
    request=EntityGroupUserRequest(
        foreign_id="MY-DB-ID-12345",
        email="john.doe@acme.com",
        name="John Doe",
        entities=[
            EntityGroupUserEntityRequest(
                roles=["admin", "approver"],
                entity_id="ent_21661ac1-a2a8-4465-a6c0-64474ba8181d",
            ),
            EntityGroupUserEntityRequest(
                roles=["viewer"],
                entity_id="ent_9e02a20e-7749-47de-8d8a-f8ff2859fa90",
            ),
        ],
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_group_id:** `EntityGroupId` — Entity Group ID or Entity Group ForeignID
    
</dd>
</dl>

<dl>
<dd>

**request:** `EntityGroupUserRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity_group.user.<a href="src/mercoa/entity_group/user/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get entity user from a group
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity_group.user.get(
    entity_group_id="entg_8545a84e-a45f-41bf-bdf1-33b42a55812c",
    foreign_id="MY-DB-ID-12345",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_group_id:** `EntityGroupId` — Entity Group ID or Entity Group ForeignID
    
</dd>
</dl>

<dl>
<dd>

**foreign_id:** `str` — ID used to identify user in your system
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity_group.user.<a href="src/mercoa/entity_group/user/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update entity user for all entities in the group.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa
from mercoa.entity_group_types import (
    EntityGroupUserEntityRequest,
    EntityGroupUserRequest,
)

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity_group.user.update(
    entity_group_id="entg_8545a84e-a45f-41bf-bdf1-33b42a55812c",
    foreign_id="MY-DB-ID-12345",
    request=EntityGroupUserRequest(
        foreign_id="MY-DB-ID-12345",
        email="john.doe@acme.com",
        name="John Doe",
        entities=[
            EntityGroupUserEntityRequest(
                roles=["admin", "approver"],
                entity_id="ent_21661ac1-a2a8-4465-a6c0-64474ba8181d",
            ),
            EntityGroupUserEntityRequest(
                roles=["viewer"],
                entity_id="ent_9e02a20e-7749-47de-8d8a-f8ff2859fa90",
            ),
        ],
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_group_id:** `EntityGroupId` — Entity Group ID or Entity Group ForeignID
    
</dd>
</dl>

<dl>
<dd>

**foreign_id:** `str` — ID used to identify user in your system
    
</dd>
</dl>

<dl>
<dd>

**request:** `EntityGroupUserRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity_group.user.<a href="src/mercoa/entity_group/user/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete entity user from all entities in the group. This will also remove the user from all approval policies. If an approval policy will break as a result of this operation, this request will fail.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity_group.user.delete(
    entity_group_id="entityGroupId",
    foreign_id="foreignId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_group_id:** `EntityGroupId` — Entity Group ID or Entity Group ForeignID
    
</dd>
</dl>

<dl>
<dd>

**foreign_id:** `str` — ID used to identify user in your system
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity_group.user.<a href="src/mercoa/entity_group/user/client.py">get_token</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generate a JWT token for an entity group with the given options. This token can be used to authenticate to any entity in the entity group as the user in the Mercoa API and iFrame.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa
from mercoa.entity_types import TokenGenerationOptions

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity_group.user.get_token(
    entity_group_id="entg_a0f6ea94-0761-4a5e-a416-3c453cb7eced",
    foreign_id="MY-DB-ID-12345",
    request=TokenGenerationOptions(
        expires_in="1h",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_group_id:** `EntityGroupId` — Entity Group ID or Entity Group ForeignID
    
</dd>
</dl>

<dl>
<dd>

**foreign_id:** `str` — ID used to identify user in your system
    
</dd>
</dl>

<dl>
<dd>

**request:** `TokenGenerationOptions` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity_group.user.<a href="src/mercoa/entity_group/user/client.py">sync</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Sync entity group users. This will add users to entities that do not have them and remove users from entities that have them.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa
from mercoa.entity_group_types import EntityGroupUserSyncRequest

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity_group.user.sync(
    entity_group_id="entg_8545a84e-a45f-41bf-bdf1-33b42a55812c",
    request=EntityGroupUserSyncRequest(
        filter_roles=["approver", "viewer"],
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_group_id:** `EntityGroupId` — Entity Group ID or Entity Group ForeignID
    
</dd>
</dl>

<dl>
<dd>

**request:** `EntityGroupUserSyncRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Entity
<details><summary><code>client.entity.<a href="src/mercoa/entity/client.py">find</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Search all entities with the given filters. If no filters are provided, all entities will be returned.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.find(
    is_customer=True,
    foreign_id="MY-DB-ID-12345",
    payment_methods=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**payment_methods:** `typing.Optional[bool]` — If true, will include entity payment methods as part of the response
    
</dd>
</dl>

<dl>
<dd>

**is_customer:** `typing.Optional[bool]` — If true, only entities with a direct relationship to the requesting organization will be returned. If false or not provided, all entities will be returned.
    
</dd>
</dl>

<dl>
<dd>

**foreign_id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — ID used to identify this entity in your system
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[typing.Union[EntityStatus, typing.Sequence[EntityStatus]]]` 
    
</dd>
</dl>

<dl>
<dd>

**is_payee:** `typing.Optional[bool]` 

If true, entities that are marked as payees will be returned.
If false or not provided, entities that are marked as payees will not be returned.
    
</dd>
</dl>

<dl>
<dd>

**is_payor:** `typing.Optional[bool]` 

If true or not provided, entities that are marked as payors will be returned.
If false, entities that are marked as payors will not be returned.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Use search instead. Deprecated. Filter entities by name. Partial matches are supported.
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` — Find entities by name, email, or emailTo. Partial matches are supported.
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[MetadataFilter]` — Filter entities by simple key/value metadata. Each filter will be applied as an AND condition. Duplicate keys will be ignored.
    
</dd>
</dl>

<dl>
<dd>

**return_metadata:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Return simple key/value metadata for the specified keys for the entities. For more complex metadata, use the Metadata API.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of entities to return. Limit can range between 1 and 100, and the default is 10.
    
</dd>
</dl>

<dl>
<dd>

**starting_after:** `typing.Optional[EntityId]` — The ID of the entity to start after. If not provided, the first page of entities will be returned.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity.<a href="src/mercoa/entity/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa
from mercoa.entity_types import (
    BusinessProfileRequest,
    EntityCreationRequest,
    ProfileRequest,
)

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.create(
    request=EntityCreationRequest(
        is_customer=False,
        is_payor=False,
        is_payee=True,
        account_type="business",
        foreign_id="MY-DB-ID-90909",
        profile=ProfileRequest(
            business=BusinessProfileRequest(
                email="vendor@bigboxstore.com",
                legal_business_name="Big Box Store",
                website="http://www.bigboxstore.com",
                business_type="publicCorporation",
            ),
        ),
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `EntityRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity.<a href="src/mercoa/entity/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.get(
    entity_id="ent_a0f6ea94-0761-4a5e-a416-3c453cb7eced",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**return_metadata:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Return simple key/value metadata for the specified keys for the entities. For more complex metadata, use the Metadata API.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity.<a href="src/mercoa/entity/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa
from mercoa.commons import Address, PhoneNumber
from mercoa.entity_types import (
    BusinessProfileRequest,
    Ein,
    EntityUpdateRequest,
    ProfileRequest,
    TaxId,
)

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.update(
    entity_id="ent_a0f6ea94-0761-4a5e-a416-3c453cb7eced",
    request=EntityUpdateRequest(
        is_customer=True,
        is_payor=True,
        is_payee=False,
        account_type="business",
        foreign_id="MY-DB-ID-12345",
        profile=ProfileRequest(
            business=BusinessProfileRequest(
                email="customer@acme.com",
                legal_business_name="Acme Inc.",
                website="http://www.acme.com",
                business_type="llc",
                phone=PhoneNumber(
                    country_code="1",
                    number="4155551234",
                ),
                address=Address(
                    address_line_1="123 Main St",
                    address_line_2="Unit 1",
                    city="San Francisco",
                    state_or_province="CA",
                    postal_code="94105",
                    country="US",
                ),
                tax_id=TaxId(
                    ein=Ein(
                        number="12-3456789",
                    ),
                ),
            ),
        ),
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**request:** `EntityUpdateRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity.<a href="src/mercoa/entity/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Will archive the entity. This action cannot be undone, and the entity will no longer be available for use. The foreignId on the entity will be cleared as well.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.delete(
    entity_id="entityId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity.<a href="src/mercoa/entity/client.py">accept_terms_of_service</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint is used to indicate acceptance of Mercoa's terms of service for an entity. Send a request to this endpoint only after the entity has accepted the Mercoa ToS. Entities must accept Mercoa ToS before they can be send or pay invoices using Mercoa's payment rails.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.accept_terms_of_service(
    entity_id="ent_a0f6ea94-0761-4a5e-a416-3c453cb7eced",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity.<a href="src/mercoa/entity/client.py">initiate_kyb</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint is used to initiate KYB for an entity. 
Send a request to this endpoint only after the entity has accepted the Mercoa ToS,
all representatives have been added, and all required fields have been filled out.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.initiate_kyb(
    entity_id="ent_a0f6ea94-0761-4a5e-a416-3c453cb7eced",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity.<a href="src/mercoa/entity/client.py">get_token</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generate a JWT token for an entity with the given options. This token can be used to authenticate the entity in the Mercoa API and iFrame.

<Warning>We recommend using [this endpoint](/api-reference/entity/user/get-token). This will enable features such as approvals and comments.</Warning>
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa
from mercoa.entity_types import TokenGenerationOptions

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.get_token(
    entity_id="ent_a0f6ea94-0761-4a5e-a416-3c453cb7eced",
    request=TokenGenerationOptions(
        expires_in="1h",
        session_id="session_123",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**request:** `TokenGenerationOptions` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity.<a href="src/mercoa/entity/client.py">get_onboarding_link</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generate an onboarding link for the entity.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.get_onboarding_link(
    entity_id="ent_a0f6ea94-0761-4a5e-a416-3c453cb7eced",
    type="PAYOR",
    expires_in="1h",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**type:** `EntityOnboardingLinkType` — The type of onboarding link to generate. If not provided, the default is payee. The onboarding options are determined by your organization's onboarding configuration.
    
</dd>
</dl>

<dl>
<dd>

**expires_in:** `typing.Optional[str]` — Expressed in seconds or a string describing a time span. The default is 24h.
    
</dd>
</dl>

<dl>
<dd>

**connected_entity_id:** `typing.Optional[EntityId]` — The ID of the entity to connect to. If onboarding a payee, this should be the payor entity ID. If onboarding a payor, this should be the payee entity ID. If no connected entity ID is provided, the onboarding link will be for a standalone entity.
    
</dd>
</dl>

<dl>
<dd>

**redirect_to_portal:** `typing.Optional[bool]` — If true, the onboarding link will redirect to the vendor/customer portal if the entity is already onboarded. If false, the onboarding link will not redirect to the portal. The default is false.
    
</dd>
</dl>

<dl>
<dd>

**vendor_portal_options:** `typing.Optional[VendorPortalOptions]` — The options for the vendor portal.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity.<a href="src/mercoa/entity/client.py">send_onboarding_link</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Send an email with a onboarding link to the entity. The email will be sent to the email address associated with the entity.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.send_onboarding_link(
    entity_id="entityId",
    type="PAYEE",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**type:** `EntityOnboardingLinkType` — The type of onboarding link to generate. If not provided, the default is payee. The onboarding options are determined by your organization's onboarding configuration.
    
</dd>
</dl>

<dl>
<dd>

**expires_in:** `typing.Optional[str]` — Expressed in seconds or a string describing a time span. The default is 7 days.
    
</dd>
</dl>

<dl>
<dd>

**connected_entity_id:** `typing.Optional[EntityId]` — The ID of the entity to connect to. If onboarding a payee, this should be the payor entity ID. If onboarding a payor, this should be the payee entity ID. If no connected entity ID is provided, the onboarding link will be for a standalone entity.
    
</dd>
</dl>

<dl>
<dd>

**redirect_to_portal:** `typing.Optional[bool]` — If true, the onboarding link will redirect to the vendor/customer portal if the entity is already onboarded. If false, the onboarding link will not redirect to the portal. The default is false.
    
</dd>
</dl>

<dl>
<dd>

**vendor_portal_options:** `typing.Optional[VendorPortalOptions]` — The options for the vendor portal.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity.<a href="src/mercoa/entity/client.py">events</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all events for an entity
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.events(
    entity_id="ent_a0f6ea94-0761-4a5e-a416-3c453cb7eced",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[dt.datetime]` — Start date filter. If not provided, events from the start of time will be returned.
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[dt.datetime]` — End date filter. If not provided, events to the end of time will be returned.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of events to return. Limit can range between 1 and 100, and the default is 50.
    
</dd>
</dl>

<dl>
<dd>

**starting_after:** `typing.Optional[EntityEventId]` — The ID of the event to start after. If not provided, the first page of events will be returned.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Entity Counterparty
<details><summary><code>client.entity.counterparty.<a href="src/mercoa/entity/counterparty/client.py">find_payees</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Find payee counterparties. This endpoint lets you find vendors linked to the entity.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.counterparty.find_payees(
    entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
    name="Big Box",
    payment_methods=True,
    invoice_metrics=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Use search instead. Deprecated. Filter counterparties by name. Partial matches are supported.
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` — Filter counterparties by name or email. Partial matches are supported.
    
</dd>
</dl>

<dl>
<dd>

**network_type:** `typing.Optional[
    typing.Union[
        CounterpartyNetworkType, typing.Sequence[CounterpartyNetworkType]
    ]
]` — Filter by network type. By default, only ENTITY counterparties are returned.
    
</dd>
</dl>

<dl>
<dd>

**payment_methods:** `typing.Optional[bool]` — If true, will include counterparty payment methods as part of the response
    
</dd>
</dl>

<dl>
<dd>

**invoice_metrics:** `typing.Optional[bool]` — If true, will include counterparty invoice metrics as part of the response
    
</dd>
</dl>

<dl>
<dd>

**counterparty_id:** `typing.Optional[typing.Union[EntityId, typing.Sequence[EntityId]]]` — Filter by counterparty ids (Foreign ID is supported)
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Union[MetadataFilter, typing.Sequence[MetadataFilter]]]` — Filter counterparties by simple key/value metadata. Each filter will be applied as an AND condition. Duplicate keys will be ignored.
    
</dd>
</dl>

<dl>
<dd>

**return_metadata:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — If true, will return simple key/value metadata for the counterparties. For more complex metadata, use the Metadata API.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of counterparties to return. Limit can range between 1 and 100, and the default is 10.
    
</dd>
</dl>

<dl>
<dd>

**starting_after:** `typing.Optional[EntityId]` — The ID of the counterparties to start after. If not provided, the first page of counterparties will be returned.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity.counterparty.<a href="src/mercoa/entity/counterparty/client.py">find_payors</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Find payor counterparties. This endpoint lets you find customers linked to the entity.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.counterparty.find_payors(
    entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
    name="Big Box",
    payment_methods=True,
    invoice_metrics=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Use search instead. Deprecated. Filter counterparties by name. Partial matches are supported.
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` — Filter counterparties by name or email. Partial matches are supported.
    
</dd>
</dl>

<dl>
<dd>

**network_type:** `typing.Optional[
    typing.Union[
        CounterpartyNetworkType, typing.Sequence[CounterpartyNetworkType]
    ]
]` — Filter by network type. By default, only ENTITY counterparties are returned.
    
</dd>
</dl>

<dl>
<dd>

**payment_methods:** `typing.Optional[bool]` — If true, will include counterparty payment methods as part of the response
    
</dd>
</dl>

<dl>
<dd>

**invoice_metrics:** `typing.Optional[bool]` — If true, will include counterparty invoice metrics as part of the response
    
</dd>
</dl>

<dl>
<dd>

**counterparty_id:** `typing.Optional[typing.Union[EntityId, typing.Sequence[EntityId]]]` — Filter by counterparty ids (Foreign ID is supported)
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Union[MetadataFilter, typing.Sequence[MetadataFilter]]]` — Filter counterparties by simple key/value metadata. Each filter will be applied as an AND condition. Duplicate keys will be ignored.
    
</dd>
</dl>

<dl>
<dd>

**return_metadata:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — If true, will return simple key/value metadata for the counterparties. For more complex metadata, use the Metadata API.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of counterparties to return. Limit can range between 1 and 100, and the default is 10.
    
</dd>
</dl>

<dl>
<dd>

**starting_after:** `typing.Optional[EntityId]` — The ID of the counterparties to start after. If not provided, the first page of counterparties will be returned.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity.counterparty.<a href="src/mercoa/entity/counterparty/client.py">add_payees</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create association between Entity and a given list of Payees. If a Payee has previously been archived, unarchive the Payee.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa
from mercoa.entity_types import (
    CounterpartyCustomizationAccount,
    CounterpartyCustomizationRequest,
    EntityAddPayeesRequest,
)

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.counterparty.add_payees(
    entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
    request=EntityAddPayeesRequest(
        payees=["ent_21661ac1-a2a8-4465-a6c0-64474ba8181d"],
        customizations=[
            CounterpartyCustomizationRequest(
                counterparty_id="ent_21661ac1-a2a8-4465-a6c0-64474ba8181d",
                accounts=[
                    CounterpartyCustomizationAccount(
                        account_id="85866843",
                        postal_code="94105",
                        name_on_account="John Doe",
                    )
                ],
            )
        ],
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**request:** `EntityAddPayeesRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity.counterparty.<a href="src/mercoa/entity/counterparty/client.py">hide_payees</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Marks Payees as unsearchable by Entity via Counterparty search. Invoices associated with these Payees will still be searchable via Invoice search.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa
from mercoa.entity_types import EntityHidePayeesRequest

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.counterparty.hide_payees(
    entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
    request=EntityHidePayeesRequest(
        payees=["ent_21661ac1-a2a8-4465-a6c0-64474ba8181d"],
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**request:** `EntityHidePayeesRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity.counterparty.<a href="src/mercoa/entity/counterparty/client.py">add_payors</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create association between Entity and a given list of Payors. If a Payor has previously been archived, unarchive the Payor.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa
from mercoa.entity_types import (
    CounterpartyCustomizationAccount,
    CounterpartyCustomizationRequest,
    EntityAddPayorsRequest,
)

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.counterparty.add_payors(
    entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
    request=EntityAddPayorsRequest(
        payors=["ent_21661ac1-a2a8-4465-a6c0-64474ba8181d"],
        customizations=[
            CounterpartyCustomizationRequest(
                counterparty_id="ent_21661ac1-a2a8-4465-a6c0-64474ba8181d",
                accounts=[
                    CounterpartyCustomizationAccount(
                        account_id="85866843",
                        postal_code="94105",
                        name_on_account="John Doe",
                    )
                ],
            )
        ],
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**request:** `EntityAddPayorsRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity.counterparty.<a href="src/mercoa/entity/counterparty/client.py">hide_payors</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Marks Payors as unsearchable by Entity via Counterparty search. Invoices associated with these Payors will still be searchable via Invoice search.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa
from mercoa.entity_types import EntityHidePayorsRequest

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.counterparty.hide_payors(
    entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
    request=EntityHidePayorsRequest(
        payors=["ent_21661ac1-a2a8-4465-a6c0-64474ba8181d"],
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**request:** `EntityHidePayorsRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Entity EmailLog
<details><summary><code>client.entity.email_log.<a href="src/mercoa/entity/email_log/client.py">find</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all incoming invoice emails for an entity.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.email_log.find(
    entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[dt.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of logs to return. Limit can range between 1 and 100, and the default is 10.
    
</dd>
</dl>

<dl>
<dd>

**starting_after:** `typing.Optional[EntityId]` — The ID of the log to start after. If not provided, the first page of logs will be returned.
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` — Search for logs by email address or subject
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity.email_log.<a href="src/mercoa/entity/email_log/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get an email log by ID
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.email_log.get(
    entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
    log_id="log_8545a84e-a45f-41bf-bdf1-33b42a55812c",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**log_id:** `EmailLogId` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Entity PaymentMethod
<details><summary><code>client.entity.payment_method.<a href="src/mercoa/entity/payment_method/client.py">get_all</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.payment_method.get_all(
    entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
    type="bankAccount",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[
    typing.Union[PaymentMethodType, typing.Sequence[PaymentMethodType]]
]` — Type of payment method to filter
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity.payment_method.<a href="src/mercoa/entity/payment_method/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa
from mercoa.payment_method_types import PaymentMethodRequest_Wallet

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.payment_method.create(
    entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
    request=PaymentMethodRequest_Wallet(),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**request:** `PaymentMethodRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity.payment_method.<a href="src/mercoa/entity/payment_method/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.payment_method.get(
    entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
    payment_method_id="pm_4794d597-70dc-4fec-b6ec-c5988e759769",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**payment_method_id:** `PaymentMethodId` — Payment Method ID or Payment Method ForeignID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity.payment_method.<a href="src/mercoa/entity/payment_method/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Only custom payment methods can be updated.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa
from mercoa.payment_method_types import PaymentMethodUpdateRequest_BankAccount

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.payment_method.update(
    entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
    payment_method_id="pm_4794d597-70dc-4fec-b6ec-c5988e759769",
    request=PaymentMethodUpdateRequest_BankAccount(
        default_source=True,
        default_destination=True,
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**payment_method_id:** `PaymentMethodId` — Payment Method ID or Payment Method ForeignID
    
</dd>
</dl>

<dl>
<dd>

**request:** `PaymentMethodUpdateRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity.payment_method.<a href="src/mercoa/entity/payment_method/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Mark a payment method as inactive. This will not remove the payment method from the system, but will prevent it from being used in the future.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.payment_method.delete(
    entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
    payment_method_id="pm_4794d597-70dc-4fec-b6ec-c5988e759769",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**payment_method_id:** `PaymentMethodId` — Payment Method ID or Payment Method ForeignID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity.payment_method.<a href="src/mercoa/entity/payment_method/client.py">plaid_link_token</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a Plaid link token for an entity. This token can be used to add or update a bank account to the entity using Plaid Link.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.payment_method.plaid_link_token(
    entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
    payment_method_id="pm_4794d597-70dc-4fec-b6ec-c5988e759769",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**payment_method_id:** `typing.Optional[PaymentMethodId]` — ID of Bank Account to update
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity.payment_method.<a href="src/mercoa/entity/payment_method/client.py">card_link_token</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a card link token for an entity. This token is used by the frontend components to generate a PCI compliant form to add a card to the entity.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.payment_method.card_link_token(
    entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity.payment_method.<a href="src/mercoa/entity/payment_method/client.py">events</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.payment_method.events(
    entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
    payment_method_id="pm_4794d597-70dc-4fec-b6ec-c5988e759769",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**payment_method_id:** `PaymentMethodId` — Payment Method ID or Payment Method ForeignID
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[dt.datetime]` — Start date filter. If not provided, events from the start of time will be returned.
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[dt.datetime]` — End date filter. If not provided, events to the end of time will be returned.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Limit the number of events returned. Limit can range between 1 and 100, and the default is 50.
    
</dd>
</dl>

<dl>
<dd>

**starting_after:** `typing.Optional[PaymentMethodEventId]` — The ID of the event to start after.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Entity User
<details><summary><code>client.entity.user.<a href="src/mercoa/entity/user/client.py">find</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Search entity users
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.user.find(
    entity_id="ent_a0f6ea94-0761-4a5e-a416-3c453cb7eced",
    name="John",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**foreign_id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — ID used to identify user in your system
    
</dd>
</dl>

<dl>
<dd>

**role:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filter users by role. If multiple roles are provided, users with any of the roles will be returned.
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Filter users by name. Partial matches are supported.
    
</dd>
</dl>

<dl>
<dd>

**email:** `typing.Optional[str]` — Filter users by email. Partial matches are supported.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of entities to return. Limit can range between 1 and 100, and the default is 10.
    
</dd>
</dl>

<dl>
<dd>

**starting_after:** `typing.Optional[EntityUserId]` — The ID of the user to start after. If not provided, the first page of entities will be returned.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity.user.<a href="src/mercoa/entity/user/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa
from mercoa.entity_types import EntityUserRequest

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.user.create(
    entity_id="ent_a0f6ea94-0761-4a5e-a416-3c453cb7eced",
    request=EntityUserRequest(
        foreign_id="MY-DB-ID-12345",
        email="john.doe@acme.com",
        name="John Doe",
        roles=["admin", "approver"],
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**request:** `EntityUserRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity.user.<a href="src/mercoa/entity/user/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get entity user
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.user.get(
    entity_id="ent_a0f6ea94-0761-4a5e-a416-3c453cb7eced",
    user_id="user_ec3aafc8-ea86-408a-a6c1-545497badbbb",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `EntityUserId` — User ID or User ForeignID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity.user.<a href="src/mercoa/entity/user/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update entity user
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa
from mercoa.entity_types import EntityUserRequest

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.user.update(
    entity_id="ent_a0f6ea94-0761-4a5e-a416-3c453cb7eced",
    user_id="user_ec3aafc8-ea86-408a-a6c1-545497badbbb",
    request=EntityUserRequest(
        foreign_id="MY-DB-ID-12345",
        email="john.doe@acme.com",
        name="John Doe",
        roles=["admin", "approver"],
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `EntityUserId` — User ID or User ForeignID
    
</dd>
</dl>

<dl>
<dd>

**request:** `EntityUserRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity.user.<a href="src/mercoa/entity/user/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete entity user. This will also remove the user from all approval policies. If an approval policy will break as a result of this operation, this request will fail.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.user.delete(
    entity_id="entityId",
    user_id="userId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `EntityUserId` — User ID or User ForeignID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity.user.<a href="src/mercoa/entity/user/client.py">get_token</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Generate a JWT token for an entity user with the given options. This token can be used to authenticate the entity and entity user in the Mercoa API and iFrame.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa
from mercoa.entity_types import TokenGenerationOptions

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.user.get_token(
    entity_id="ent_a0f6ea94-0761-4a5e-a416-3c453cb7eced",
    user_id="user_a0f6ea94-0761-4a5e-a416-3c453cb7eced",
    request=TokenGenerationOptions(
        expires_in="1h",
        session_id="session_123",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `EntityId` — Entity ID or Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**user_id:** `EntityUserId` — User ID or User ForeignID
    
</dd>
</dl>

<dl>
<dd>

**request:** `TokenGenerationOptions` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## InvoiceTemplate
<details><summary><code>client.invoice_template.<a href="src/mercoa/invoice_template/client.py">find</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Search invoice templates for all entities in the organization
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.invoice_template.find(
    entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `typing.Optional[typing.Union[EntityId, typing.Sequence[EntityId]]]` — Filter invoice templates by the ID or foreign ID of the entity that is the payer or the vendor of the invoice template.
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[dt.datetime]` — Start date filter. Defaults to CREATED_AT unless specified the dateType is specified
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[dt.datetime]` — End date filter. Defaults to CREATED_AT unless specified the dateType is specified
    
</dd>
</dl>

<dl>
<dd>

**date_type:** `typing.Optional[InvoiceDateFilter]` — Type of date to filter by if startDate and endDate filters are provided. Defaults to CREATED_AT.
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[InvoiceOrderByField]` — Field to order invoice templates by. Defaults to CREATED_AT.
    
</dd>
</dl>

<dl>
<dd>

**order_direction:** `typing.Optional[OrderDirection]` — Direction to order invoice templates by. Defaults to asc.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of invoice templates to return. Limit can range between 1 and 100, and the default is 10.
    
</dd>
</dl>

<dl>
<dd>

**starting_after:** `typing.Optional[InvoiceTemplateId]` — The ID of the invoice template to start after. If not provided, the first page of invoice templates will be returned.
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` — Find invoice templates by vendor name, check number, invoice number, or amount. Partial matches are supported.
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Union[MetadataFilter, typing.Sequence[MetadataFilter]]]` — Filter invoice templates by metadata. Each filter will be applied as an AND condition. Duplicate keys will be ignored.
    
</dd>
</dl>

<dl>
<dd>

**line_item_metadata:** `typing.Optional[typing.Union[MetadataFilter, typing.Sequence[MetadataFilter]]]` — Filter invoice templates by line item metadata. Each filter will be applied as an AND condition. Duplicate keys will be ignored.
    
</dd>
</dl>

<dl>
<dd>

**line_item_gl_account_id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filter invoice templates by line item GL account ID. Each filter will be applied as an OR condition. Duplicate keys will be ignored.
    
</dd>
</dl>

<dl>
<dd>

**payer_id:** `typing.Optional[typing.Union[EntityId, typing.Sequence[EntityId]]]` — Filter invoice templates by payer ID or payer foreign ID.
    
</dd>
</dl>

<dl>
<dd>

**vendor_id:** `typing.Optional[typing.Union[EntityId, typing.Sequence[EntityId]]]` — Filter invoice templates by vendor ID or vendor foreign ID.
    
</dd>
</dl>

<dl>
<dd>

**creator_user_id:** `typing.Optional[typing.Union[EntityUserId, typing.Sequence[EntityUserId]]]` — Filter invoices by the ID or foreign ID of the user that created the invoice.
    
</dd>
</dl>

<dl>
<dd>

**approver_id:** `typing.Optional[typing.Union[EntityUserId, typing.Sequence[EntityUserId]]]` — Filter invoice templates by assigned approver user ID.
    
</dd>
</dl>

<dl>
<dd>

**approver_action:** `typing.Optional[typing.Union[ApproverAction, typing.Sequence[ApproverAction]]]` — Filter invoice templates by approver action. Needs to be used with approverId. For example, if you want to find all invoice templates that have been approved by a specific user, you would use approverId and approverAction=APPROVE.
    
</dd>
</dl>

<dl>
<dd>

**invoice_id:** `typing.Optional[typing.Union[InvoiceId, typing.Sequence[InvoiceId]]]` — Filter invoice templates by invoice ID.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[typing.Union[InvoiceStatus, typing.Sequence[InvoiceStatus]]]` — Invoice status to filter on
    
</dd>
</dl>

<dl>
<dd>

**payment_type:** `typing.Optional[typing.Sequence[PaymentType]]` — Filter invoice templates by recurring status
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.invoice_template.<a href="src/mercoa/invoice_template/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime

from mercoa import Mercoa
from mercoa.invoice_types import (
    InvoiceLineItemCreationRequest,
    InvoiceTemplateCreationRequest,
    PaymentDestinationOptions_Check,
    PaymentSchedule_Monthly,
)

client = Mercoa(
    token="YOUR_TOKEN",
)
client.invoice_template.create(
    request=InvoiceTemplateCreationRequest(
        status="NEW",
        amount=100.0,
        currency="USD",
        invoice_date=datetime.datetime.fromisoformat(
            "2021-01-01 00:00:00+00:00",
        ),
        due_date=datetime.datetime.fromisoformat(
            "2021-01-13 00:00:00+00:00",
        ),
        deduction_date=datetime.datetime.fromisoformat(
            "2021-01-10 00:00:00+00:00",
        ),
        payment_schedule=PaymentSchedule_Monthly(
            repeat_on_day=10,
            ends=datetime.datetime.fromisoformat(
                "2021-01-01 00:00:00+00:00",
            ),
        ),
        invoice_number="INV-123",
        note_to_self="Monthly recurring payment",
        payer_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
        payment_source_id="pm_4794d597-70dc-4fec-b6ec-c5988e759769",
        vendor_id="ent_21661ac1-a2a8-4465-a6c0-64474ba8181d",
        payment_destination_id="pm_5fde2f4a-facc-48ef-8f0d-6b7d087c7b18",
        payment_destination_options=PaymentDestinationOptions_Check(
            delivery="MAIL",
            print_description=True,
        ),
        line_items=[
            InvoiceLineItemCreationRequest(
                amount=100.0,
                currency="USD",
                description="Product A",
                name="Product A",
                quantity=1.0,
                unit_price=100.0,
                category="EXPENSE",
                service_start_date=datetime.datetime.fromisoformat(
                    "2021-01-01 00:00:00+00:00",
                ),
                service_end_date=datetime.datetime.fromisoformat(
                    "2021-01-31 00:00:00+00:00",
                ),
                metadata={"key1": "value1", "key2": "value2"},
                gl_account_id="600394",
            )
        ],
        creator_entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
        creator_user_id="user_e24fc81c-c5ee-47e8-af42-4fe29d895506",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `InvoiceTemplateCreationRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.invoice_template.<a href="src/mercoa/invoice_template/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.invoice_template.get(
    invoice_template_id="invt_13c07096-5848-4aeb-ae7d-6576289034c4",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**invoice_template_id:** `InvoiceTemplateId` — Invoice Template ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.invoice_template.<a href="src/mercoa/invoice_template/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime

from mercoa import Mercoa
from mercoa.invoice_types import (
    InvoiceLineItemUpdateRequest,
    InvoiceTemplateUpdateRequest,
    PaymentDestinationOptions_Check,
)

client = Mercoa(
    token="YOUR_TOKEN",
)
client.invoice_template.update(
    invoice_template_id="invt_13c07096-5848-4aeb-ae7d-6576289034c4",
    request=InvoiceTemplateUpdateRequest(
        status="NEW",
        amount=100.0,
        currency="USD",
        invoice_date=datetime.datetime.fromisoformat(
            "2021-01-01 00:00:00+00:00",
        ),
        due_date=datetime.datetime.fromisoformat(
            "2021-01-31 00:00:00+00:00",
        ),
        invoice_number="INV-123",
        note_to_self="For the month of January",
        payer_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
        payment_source_id="pm_4794d597-70dc-4fec-b6ec-c5988e759769",
        vendor_id="ent_21661ac1-a2a8-4465-a6c0-64474ba8181d",
        payment_destination_id="pm_5fde2f4a-facc-48ef-8f0d-6b7d087c7b18",
        payment_destination_options=PaymentDestinationOptions_Check(
            delivery="MAIL",
            print_description=True,
        ),
        line_items=[
            InvoiceLineItemUpdateRequest(
                id="inli_26672f38-eb9a-48f1-a7a0-f1b855e38cd7",
                amount=100.0,
                currency="USD",
                description="Product A",
                name="Product A",
                quantity=1.0,
                unit_price=100.0,
                category="EXPENSE",
                service_start_date=datetime.datetime.fromisoformat(
                    "2021-01-01 00:00:00+00:00",
                ),
                service_end_date=datetime.datetime.fromisoformat(
                    "2021-01-31 00:00:00+00:00",
                ),
                metadata={"key1": "value1", "key2": "value2"},
                gl_account_id="600394",
            )
        ],
        creator_entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
        creator_user_id="user_e24fc81c-c5ee-47e8-af42-4fe29d895506",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**invoice_template_id:** `InvoiceTemplateId` — Invoice Template ID
    
</dd>
</dl>

<dl>
<dd>

**request:** `InvoiceTemplateUpdateRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.invoice_template.<a href="src/mercoa/invoice_template/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Only invoice templates in the UNASSIGNED and DRAFT statuses can be deleted.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.invoice_template.delete(
    invoice_template_id="invt_13c07096-5848-4aeb-ae7d-6576289034c4",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**invoice_template_id:** `InvoiceTemplateId` — Invoice Template ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## InvoiceTemplate LineItem
<details><summary><code>client.invoice_template.line_item.<a href="src/mercoa/invoice_template/line_item/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update invoice template line item
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
import datetime

from mercoa import Mercoa
from mercoa.invoice_types import InvoiceLineItemIndividualUpdateRequest

client = Mercoa(
    token="YOUR_TOKEN",
)
client.invoice_template.line_item.update(
    invoice_template_id="invt_13c07096-5848-4aeb-ae7d-6576289034c4",
    line_item_id="inli_8aa84cb8-2ae7-4579-8fa3-87586e7c14a7",
    request=InvoiceLineItemIndividualUpdateRequest(
        name="Product A",
        description="Product A",
        service_start_date=datetime.datetime.fromisoformat(
            "2021-01-01 00:00:00+00:00",
        ),
        service_end_date=datetime.datetime.fromisoformat(
            "2021-01-31 00:00:00+00:00",
        ),
        metadata={"key1": "value1", "key2": "value2"},
        gl_account_id="600394",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**invoice_template_id:** `InvoiceTemplateId` — Invoice Template ID
    
</dd>
</dl>

<dl>
<dd>

**line_item_id:** `InvoiceLineItemId` — Invoice Line Item ID
    
</dd>
</dl>

<dl>
<dd>

**request:** `InvoiceLineItemIndividualUpdateRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Invoice
<details><summary><code>client.invoice.<a href="src/mercoa/invoice/client.py">find</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Search invoices for all entities in the organization
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa

client = Mercoa(
    token="YOUR_TOKEN",
)
client.invoice.find(
    entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**entity_id:** `typing.Optional[typing.Union[EntityId, typing.Sequence[EntityId]]]` — Filter invoices by the ID or foreign ID of the entity that is the payer or the vendor of the invoice.
    
</dd>
</dl>

<dl>
<dd>

**entity_group_id:** `typing.Optional[EntityGroupId]` — Filter invoices by the ID or foreign ID of the entity group that the entity belongs to.
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[dt.datetime]` — Start date filter. Defaults to CREATED_AT unless specified the dateType is specified
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[dt.datetime]` — End date filter. Defaults to CREATED