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

**order_by:** `typing.Optional[InvoiceOrderByField]` — Field to order invoices by. Defaults to CREATED_AT.
    
</dd>
</dl>

<dl>
<dd>

**order_direction:** `typing.Optional[OrderDirection]` — Direction to order invoices by. Defaults to asc.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of invoices to return. Limit can range between 1 and 100, and the default is 10.
    
</dd>
</dl>

<dl>
<dd>

**starting_after:** `typing.Optional[InvoiceId]` — The ID of the invoice to start after. If not provided, the first page of invoices will be returned.
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` — Find invoices by vendor name, invoice number, check number, or amount. Partial matches are supported.
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Union[MetadataFilter, typing.Sequence[MetadataFilter]]]` — Filter invoices by metadata. Each filter will be applied as an AND condition. Duplicate keys will be ignored.
    
</dd>
</dl>

<dl>
<dd>

**line_item_metadata:** `typing.Optional[typing.Union[MetadataFilter, typing.Sequence[MetadataFilter]]]` — Filter invoices by line item metadata. Each filter will be applied as an AND condition. Duplicate keys will be ignored.
    
</dd>
</dl>

<dl>
<dd>

**line_item_gl_account_id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filter invoices by line item GL account ID. Each filter will be applied as an OR condition. Duplicate keys will be ignored.
    
</dd>
</dl>

<dl>
<dd>

**payer_id:** `typing.Optional[typing.Union[EntityId, typing.Sequence[EntityId]]]` — Filter invoices by payer ID or payer foreign ID.
    
</dd>
</dl>

<dl>
<dd>

**vendor_id:** `typing.Optional[typing.Union[EntityId, typing.Sequence[EntityId]]]` — Filter invoices by vendor ID or vendor foreign ID.
    
</dd>
</dl>

<dl>
<dd>

**creator_user_id:** `typing.Optional[typing.Union[EntityUserId, typing.Sequence[EntityUserId]]]` — Filter invoices by the ID or foreign ID of the user that created the invoice.
    
</dd>
</dl>

<dl>
<dd>

**approver_id:** `typing.Optional[typing.Union[EntityUserId, typing.Sequence[EntityUserId]]]` — Filter invoices by assigned approver user ID. Only invoices with all upstream policies approved will be returned.
    
</dd>
</dl>

<dl>
<dd>

**approver_action:** `typing.Optional[typing.Union[ApproverAction, typing.Sequence[ApproverAction]]]` — Filter invoices by approver action. Needs to be used with approverId. For example, if you want to find all invoices that have been approved by a specific user, you would use approverId and approverAction=APPROVE.
    
</dd>
</dl>

<dl>
<dd>

**invoice_id:** `typing.Optional[typing.Union[InvoiceId, typing.Sequence[InvoiceId]]]` — Filter invoices by invoice ID or invoice foreign ID.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[typing.Union[InvoiceStatus, typing.Sequence[InvoiceStatus]]]` — Invoice status to filter on
    
</dd>
</dl>

<dl>
<dd>

**payment_type:** `typing.Optional[typing.Sequence[PaymentType]]` — Filter invoices by recurring status
    
</dd>
</dl>

<dl>
<dd>

**invoice_template_id:** `typing.Optional[
    typing.Union[InvoiceTemplateId, typing.Sequence[InvoiceTemplateId]]
]` — Filter invoice by invoice template ID
    
</dd>
</dl>

<dl>
<dd>

**return_payer_metadata:** `typing.Optional[bool]` — Whether to return payer metadata in the response
    
</dd>
</dl>

<dl>
<dd>

**return_vendor_metadata:** `typing.Optional[bool]` — Whether to return vendor metadata in the response
    
</dd>
</dl>

<dl>
<dd>

**return_payment_timing:** `typing.Optional[bool]` — Whether to return payment timing in the response
    
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

<details><summary><code>client.invoice.<a href="src/mercoa/invoice/client.py">create</a>(...)</code></summary>
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
from mercoa.invoice_types import InvoiceCreationWithEntityRequest

client = Mercoa(
    token="YOUR_TOKEN",
)
client.invoice.create(
    request=InvoiceCreationWithEntityRequest(
        status="SCHEDULED",
        payer_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
        creator_entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
        vendor_id="ent_21661ac1-a2a8-4465-a6c0-64474ba8181d",
        currency="USD",
        amount=100.0,
        invoice_date=datetime.datetime.fromisoformat(
            "2021-01-01 00:00:00+00:00",
        ),
        due_date=datetime.datetime.fromisoformat(
            "2021-01-31 00:00:00+00:00",
        ),
        payment_source_id="pm_4794d597-70dc-4fec-b6ec-c5988e759769",
        payment_destination_id="pm_5fde2f4a-facc-48ef-8f0d-6b7d087c7b18",
        deduction_date=datetime.datetime.fromisoformat(
            "2021-01-29 00:00:00+00:00",
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

**request:** `InvoiceCreationRequest` 
    
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

<details><summary><code>client.invoice.<a href="src/mercoa/invoice/client.py">get</a>(...)</code></summary>
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
client.invoice.get(
    invoice_id="in_8545a84e-a45f-41bf-bdf1-33b42a55812c",
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

**invoice_id:** `InvoiceId` — Invoice ID or Invoice ForeignID
    
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

<details><summary><code>client.invoice.<a href="src/mercoa/invoice/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa
from mercoa.invoice_types import InvoiceUpdateRequest

client = Mercoa(
    token="YOUR_TOKEN",
)
client.invoice.update(
    invoice_id="in_26e7b5d3-a739-4b23-9ad9-6aaa085f47a9",
    request=InvoiceUpdateRequest(
        vendor_credit_ids=["vcr_c3f4c87d-794d-4543-9562-575cdddfc0d7"],
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

**invoice_id:** `InvoiceId` — Invoice ID or Invoice ForeignID
    
</dd>
</dl>

<dl>
<dd>

**request:** `InvoiceUpdateRequest` 
    
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

<details><summary><code>client.invoice.<a href="src/mercoa/invoice/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Only invoices in the UNASSIGNED and DRAFT statuses can be deleted.
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
client.invoice.delete(
    invoice_id="in_8545a84e-a45f-41bf-bdf1-33b42a55812c",
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

**invoice_id:** `InvoiceId` — Invoice ID or Invoice ForeignID
    
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

<details><summary><code>client.invoice.<a href="src/mercoa/invoice/client.py">events</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all events for an invoice
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
client.invoice.events(
    invoice_id="in_8545a84e-a45f-41bf-bdf1-33b42a55812c",
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

**invoice_id:** `InvoiceId` — Invoice ID or Invoice ForeignID
    
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

**starting_after:** `typing.Optional[InvoiceEventId]` — The ID of the event to start after. If not provided, the first page of events will be returned.
    
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

## Invoice LineItem
<details><summary><code>client.invoice.line_item.<a href="src/mercoa/invoice/line_item/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update invoice line item
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
client.invoice.line_item.update(
    invoice_id="in_d8f68285-1c6d-4d5a-a9e3-252c3180fac4",
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

**invoice_id:** `InvoiceId` — Invoice ID
    
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

## Organization
<details><summary><code>client.organization.<a href="src/mercoa/organization/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get current organization information
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
client.organization.get()

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

**payment_methods:** `typing.Optional[bool]` — include supported payment methods in response
    
</dd>
</dl>

<dl>
<dd>

**email_provider:** `typing.Optional[bool]` — include email provider info in response
    
</dd>
</dl>

<dl>
<dd>

**external_accounting_system_provider:** `typing.Optional[bool]` — include external accounting system provider info in response
    
</dd>
</dl>

<dl>
<dd>

**color_scheme:** `typing.Optional[bool]` — include color scheme info in response
    
</dd>
</dl>

<dl>
<dd>

**payee_onboarding_options:** `typing.Optional[bool]` — include payee onboarding options in response
    
</dd>
</dl>

<dl>
<dd>

**payor_onboarding_options:** `typing.Optional[bool]` — include payor onboarding options in response
    
</dd>
</dl>

<dl>
<dd>

**metadata_schema:** `typing.Optional[bool]` — include metadata schema in response
    
</dd>
</dl>

<dl>
<dd>

**notification_email_template:** `typing.Optional[bool]` — include notification-email-template in response
    
</dd>
</dl>

<dl>
<dd>

**role_permissions:** `typing.Optional[bool]` — include role permission config in response
    
</dd>
</dl>

<dl>
<dd>

**custom_domains:** `typing.Optional[bool]` — include custom domains in response
    
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

<details><summary><code>client.organization.<a href="src/mercoa/organization/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update current organization
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
from mercoa.organization_types import OrganizationRequest

client = Mercoa(
    token="YOUR_TOKEN",
)
client.organization.update(
    request=OrganizationRequest(),
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

**request:** `OrganizationRequest` 
    
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

<details><summary><code>client.organization.<a href="src/mercoa/organization/client.py">email_log</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get log of all emails sent to this organization. Content format subject to change.
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
client.organization.email_log()

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

**from_:** `typing.Optional[str]` — Filter by sender email address
    
</dd>
</dl>

<dl>
<dd>

**to:** `typing.Optional[str]` — Filter by recipient email address
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of logs to return. Limit can range between 1 and 100, and the default is 10.
    
</dd>
</dl>

<dl>
<dd>

**starting_after:** `typing.Optional[str]` — The ID of the log to start after. If not provided, the first page of logs will be returned.
    
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

<details><summary><code>client.organization.<a href="src/mercoa/organization/client.py">invalidate_tokens</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Invalidate all JWT tokens for the current organization. This is considered a break-glass action and should be used only if tokens have been compromised. All tokens will be invalidated, including tokens on links, emails, and currently logged in sessions. API keys are not affected by this action. This action may take 60 seconds to propagate.
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
client.organization.invalidate_tokens()

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

**session_id:** `typing.Optional[typing.Sequence[str]]` — Optional list of session IDs to invalidate. If not provided, all sessions will be invalidated.
    
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

## PaymentGateway
<details><summary><code>client.payment_gateway.<a href="src/mercoa/payment_gateway/client.py">create_validation_job</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a job to validate a payment gateway
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
from mercoa.payment_gateway_types import ValidatePaymentGatewayRequest_Html

client = Mercoa(
    token="YOUR_TOKEN",
)
client.payment_gateway.create_validation_job(
    request=ValidatePaymentGatewayRequest_Html(
        html='<html><body><h1>Invoice Details</h1><a href="https://www.payment-gateway.com/invoice/job_1a92b5f7-f522-435e-a953-fd649363730a4567890">Pay Invoice</a></body></html>',
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

**request:** `ValidatePaymentGatewayRequest` 
    
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

<details><summary><code>client.payment_gateway.<a href="src/mercoa/payment_gateway/client.py">get_validation_job</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the status of a payment gateway validation job
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
client.payment_gateway.get_validation_job(
    job_id="job_1a92b5f7-f522-435e-a953-fd649363730a",
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

**job_id:** `str` — The ID of the payment gateway validation job
    
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

<details><summary><code>client.payment_gateway.<a href="src/mercoa/payment_gateway/client.py">create_process_job</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a job to process a payment through a payment gateway
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
from mercoa.payment_gateway_types import (
    ProcessPaymentGatewayCardDetails_Iframe,
    ProcessPaymentGatewayRequest_Html,
)

client = Mercoa(
    token="YOUR_TOKEN",
)
client.payment_gateway.create_process_job(
    request=ProcessPaymentGatewayRequest_Html(
        html='<html><body><h1>Invoice Details</h1><a href="https://www.payment-gateway.com/invoice/123123">Pay Invoice</a></body></html>',
        card_details=ProcessPaymentGatewayCardDetails_Iframe(
            first_name="John",
            last_name="Doe",
            postal_code="12345",
            country="US",
            iframe_url="https://www.myvirtualcard.com/iframe/543543",
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

**request:** `ProcessPaymentGatewayRequest` 
    
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

<details><summary><code>client.payment_gateway.<a href="src/mercoa/payment_gateway/client.py">get_process_job</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the status of a payment gateway processing job
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
client.payment_gateway.get_process_job(
    job_id="job_1a92b5f7-f522-435e-a953-fd649363730a",
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

**job_id:** `str` — The ID of the payment gateway processing job
    
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

## BankLookup
<details><summary><code>client.bank_lookup.<a href="src/mercoa/bank_lookup/client.py">find</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Find bank account details
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
client.bank_lookup.find(
    routing_number="026009593",
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

**routing_number:** `str` — Routing number to validate
    
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

## Calculate
<details><summary><code>client.calculate.<a href="src/mercoa/calculate/client.py">fee</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Calculate the estimated fees associated with an payment given the amount, payment source, and disbursement method. Can be used to calculate fees for a payment before creating an invoice.
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
from mercoa.calculate import CalculateFeesRequest

client = Mercoa(
    token="YOUR_TOKEN",
)
client.calculate.fee(
    request=CalculateFeesRequest(
        amount=100.0,
        payment_source_id="pm_4794d597-70dc-4fec-b6ec-c5988e759769",
        payment_destination_id="pm_4794d597-70dc-4fec-b6ec-c5988e759769",
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

**request:** `CalculateFeesRequest` 
    
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

<details><summary><code>client.calculate.<a href="src/mercoa/calculate/client.py">payment_timing</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Calculate the estimated payment timing given the deduction date, payment source, and disbursement method. Can be used to calculate timing for a payment.
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
from mercoa.calculate import InvoiceTiming

client = Mercoa(
    token="YOUR_TOKEN",
)
client.calculate.payment_timing(
    request=InvoiceTiming(
        invoice_id="in_26e7b5d3-a739-4b23-9ad9-6aaa085f47a9",
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

**request:** `CalculatePaymentTimingRequest` 
    
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

## CustomPaymentMethodSchema
<details><summary><code>client.custom_payment_method_schema.<a href="src/mercoa/custom_payment_method_schema/client.py">get_all</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all custom payment method schemas
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
client.custom_payment_method_schema.get_all()

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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.custom_payment_method_schema.<a href="src/mercoa/custom_payment_method_schema/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create custom payment method schema
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
from mercoa.payment_method_types import (
    CustomPaymentMethodSchemaField,
    CustomPaymentMethodSchemaRequest,
)

client = Mercoa(
    token="YOUR_TOKEN",
)
client.custom_payment_method_schema.create(
    request=CustomPaymentMethodSchemaRequest(
        name="Check",
        is_source=False,
        is_destination=True,
        supported_currencies=["USD"],
        fields=[
            CustomPaymentMethodSchemaField(
                name="payToTheOrderOf",
                display_name="Pay To The Order Of",
                type="text",
                optional=False,
            ),
            CustomPaymentMethodSchemaField(
                name="accountNumber",
                display_name="Account Number",
                type="usBankAccountNumber",
                optional=False,
                use_as_account_number=True,
            ),
            CustomPaymentMethodSchemaField(
                name="routingNumber",
                display_name="Routing Number",
                type="usBankRoutingNumber",
                optional=False,
            ),
            CustomPaymentMethodSchemaField(
                name="address",
                display_name="Address",
                type="address",
                optional=False,
            ),
        ],
        estimated_processing_time=7,
        max_amount=50000.0,
        min_amount=1.0,
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

**request:** `CustomPaymentMethodSchemaRequest` 
    
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

<details><summary><code>client.custom_payment_method_schema.<a href="src/mercoa/custom_payment_method_schema/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update custom payment method schema
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
from mercoa.payment_method_types import (
    CustomPaymentMethodSchemaField,
    CustomPaymentMethodSchemaRequest,
)

client = Mercoa(
    token="YOUR_TOKEN",
)
client.custom_payment_method_schema.update(
    schema_id="cpms_14f78dcd-4614-426e-a37a-7af262431d41",
    request=CustomPaymentMethodSchemaRequest(
        name="Wire",
        is_source=False,
        is_destination=True,
        supported_currencies=["USD", "EUR"],
        fields=[
            CustomPaymentMethodSchemaField(
                name="bankName",
                display_name="Bank Name",
                type="text",
                optional=False,
            ),
            CustomPaymentMethodSchemaField(
                name="recipientName",
                display_name="Recipient Name",
                type="text",
                optional=False,
            ),
            CustomPaymentMethodSchemaField(
                name="accountNumber",
                display_name="Account Number",
                type="usBankAccountNumber",
                optional=False,
                use_as_account_number=True,
            ),
            CustomPaymentMethodSchemaField(
                name="routingNumber",
                display_name="Routing Number",
                type="usBankRoutingNumber",
                optional=False,
            ),
        ],
        estimated_processing_time=0,
        max_amount=100000.0,
        min_amount=1.0,
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

**schema_id:** `CustomPaymentMethodSchemaId` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `CustomPaymentMethodSchemaRequest` 
    
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

<details><summary><code>client.custom_payment_method_schema.<a href="src/mercoa/custom_payment_method_schema/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get custom payment method schema
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
client.custom_payment_method_schema.get(
    schema_id="cpms_14f78dcd-4614-426e-a37a-7af262431d41",
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

**schema_id:** `CustomPaymentMethodSchemaId` 
    
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

<details><summary><code>client.custom_payment_method_schema.<a href="src/mercoa/custom_payment_method_schema/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete custom payment method schema. Schema that have been used in an invoice cannot be deleted.
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
client.custom_payment_method_schema.delete(
    schema_id="cpms_14f78dcd-4614-426e-a37a-7af262431d41",
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

**schema_id:** `CustomPaymentMethodSchemaId` 
    
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

## EntityGroup Invoice
<details><summary><code>client.entity_group.invoice.<a href="src/mercoa/entity_group/invoice/client.py">find</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get invoices for an entity group with the given filters.
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
client.entity_group.invoice.find(
    entity_group_id="entg_8545a84e-a45f-41bf-bdf1-33b42a55812c",
    exclude_receivables=True,
    order_by="CREATED_AT",
    order_direction="ASC",
    limit=10,
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

**exclude_payables:** `typing.Optional[bool]` — Return only invoices that are receivable by the entity.
    
</dd>
</dl>

<dl>
<dd>

**exclude_receivables:** `typing.Optional[bool]` — Return only invoices that are payable by the entity.
    
</dd>
</dl>

<dl>
<dd>

**start_date:** `typing.Optional[dt.datetime]` — Start date for invoice created on date filter.
    
</dd>
</dl>

<dl>
<dd>

**end_date:** `typing.Optional[dt.datetime]` — End date for invoice created date filter.
    
</dd>
</dl>

<dl>
<dd>

**date_type:** `typing.Optional[InvoiceDateFilter]` — Type of date to filter by if startDate and endDate filters are provided. Defaults to CREATED_AT.
    
</dd>
</dl>

<dl>
<dd>

**order_by:** `typing.Optional[InvoiceOrderByField]` — Field to order invoices by. Defaults to CREATED_AT.
    
</dd>
</dl>

<dl>
<dd>

**order_direction:** `typing.Optional[OrderDirection]` — Direction to order invoices by. Defaults to asc.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of invoices to return. Limit can range between 1 and 100, and the default is 10.
    
</dd>
</dl>

<dl>
<dd>

**starting_after:** `typing.Optional[InvoiceId]` — The ID of the invoice to start after. If not provided, the first page of invoices will be returned.
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Union[MetadataFilter, typing.Sequence[MetadataFilter]]]` — Filter invoices by metadata. Each filter will be applied as an AND condition. Duplicate keys will be ignored.
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` — Find invoices by vendor name, invoice number, check number, or amount. Partial matches are supported.
    
</dd>
</dl>

<dl>
<dd>

**payer_id:** `typing.Optional[typing.Union[EntityId, typing.Sequence[EntityId]]]` — Filter invoices by payer ID or payer foreign ID.
    
</dd>
</dl>

<dl>
<dd>

**vendor_id:** `typing.Optional[typing.Union[EntityId, typing.Sequence[EntityId]]]` — Filter invoices by vendor ID or vendor foreign ID.
    
</dd>
</dl>

<dl>
<dd>

**creator_user_id:** `typing.Optional[typing.Union[EntityUserId, typing.Sequence[EntityUserId]]]` — Filter invoices by the ID or foreign ID of the user that created the invoice.
    
</dd>
</dl>

<dl>
<dd>

**approver_id:** `typing.Optional[typing.Union[EntityUserId, typing.Sequence[EntityUserId]]]` — Filter invoices by assigned approver user ID.
    
</dd>
</dl>

<dl>
<dd>

**approver_action:** `typing.Optional[typing.Union[ApproverAction, typing.Sequence[ApproverAction]]]` — Filter invoices by approver action. Needs to be used with approverId. For example, if you want to find all invoices that have been approved by a specific user, you would use approverId and approverAction=APPROVE.
    
</dd>
</dl>

<dl>
<dd>

**invoice_id:** `typing.Optional[typing.Union[InvoiceId, typing.Sequence[InvoiceId]]]` — Filter invoices by invoice ID or invoice foreign ID.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[typing.Union[InvoiceStatus, typing.Sequence[InvoiceStatus]]]` — Invoice status to filter on.
    
</dd>
</dl>

<dl>
<dd>

**payment_type:** `typing.Optional[typing.Sequence[PaymentType]]` — Filter invoices by recurring status
    
</dd>
</dl>

<dl>
<dd>

**return_payer_metadata:** `typing.Optional[bool]` — Whether to return payer metadata in the response
    
</dd>
</dl>

<dl>
<dd>

**return_vendor_metadata:** `typing.Optional[bool]` — Whether to return vendor metadata in the response
    
</dd>
</dl>

<dl>
<dd>

**return_payment_timing:** `typing.Optional[bool]` — Whether to return payment timing in the response
    
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

<details><summary><code>client.entity_group.invoice.<a href="src/mercoa/entity_group/invoice/client.py">download</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a URL to download invoices for an entity group as a CSV/JSON file.
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
client.entity_group.invoice.download(
    entity_group_id="entg_8545a84e-a45f-41bf-bdf1-33b42a55812c",
    format="CSV",
    exclude_receivables=True,
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

**format:** `typing.Optional[BulkDownloadFormat]` — Format of the file to download. Defaults to CSV.
    
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

**order_by:** `typing.Optional[InvoiceOrderByField]` — Field to order invoices by. Defaults to CREATED_AT.
    
</dd>
</dl>

<dl>
<dd>

**order_direction:** `typing.Optional[OrderDirection]` — Direction to order invoices by. Defaults to asc.
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` — Find invoices by vendor name, invoice number, check number, or amount. Partial matches are supported.
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Union[MetadataFilter, typing.Sequence[MetadataFilter]]]` — Filter invoices by metadata. Each filter will be applied as an AND condition. Duplicate keys will be ignored.
    
</dd>
</dl>

<dl>
<dd>

**line_item_metadata:** `typing.Optional[typing.Union[MetadataFilter, typing.Sequence[MetadataFilter]]]` — Filter invoices by line item metadata. Each filter will be applied as an AND condition. Duplicate keys will be ignored.
    
</dd>
</dl>

<dl>
<dd>

**line_item_gl_account_id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filter invoices by line item GL account ID. Each filter will be applied as an OR condition. Duplicate keys will be ignored.
    
</dd>
</dl>

<dl>
<dd>

**payer_id:** `typing.Optional[typing.Union[EntityId, typing.Sequence[EntityId]]]` — Filter invoices by payer ID or payer foreign ID.
    
</dd>
</dl>

<dl>
<dd>

**vendor_id:** `typing.Optional[typing.Union[EntityId, typing.Sequence[EntityId]]]` — Filter invoices by vendor ID or vendor foreign ID.
    
</dd>
</dl>

<dl>
<dd>

**creator_user_id:** `typing.Optional[typing.Union[EntityUserId, typing.Sequence[EntityUserId]]]` — Filter invoices by the ID or foreign ID of the user that created the invoice.
    
</dd>
</dl>

<dl>
<dd>

**approver_id:** `typing.Optional[typing.Union[EntityUserId, typing.Sequence[EntityUserId]]]` — Filter invoices by assigned approver user ID. Only invoices with all upstream policies approved will be returned.
    
</dd>
</dl>

<dl>
<dd>

**approver_action:** `typing.Optional[typing.Union[ApproverAction, typing.Sequence[ApproverAction]]]` — Filter invoices by approver action. Needs to be used with approverId. For example, if you want to find all invoices that have been approved by a specific user, you would use approverId and approverAction=APPROVE.
    
</dd>
</dl>

<dl>
<dd>

**invoice_id:** `typing.Optional[typing.Union[InvoiceId, typing.Sequence[InvoiceId]]]` — Filter invoices by invoice ID or invoice foreign ID.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[typing.Union[InvoiceStatus, typing.Sequence[InvoiceStatus]]]` — Invoice status to filter on
    
</dd>
</dl>

<dl>
<dd>

**payment_type:** `typing.Optional[typing.Sequence[PaymentType]]` — Filter invoices by recurring status
    
</dd>
</dl>

<dl>
<dd>

**invoice_template_id:** `typing.Optional[
    typing.Union[InvoiceTemplateId, typing.Sequence[InvoiceTemplateId]]
]` — Filter invoice by invoice template ID
    
</dd>
</dl>

<dl>
<dd>

**exclude_payables:** `typing.Optional[bool]` — Return only invoices that are receivable by the entity.
    
</dd>
</dl>

<dl>
<dd>

**exclude_receivables:** `typing.Optional[bool]` — Return only invoices that are payable by the entity.
    
</dd>
</dl>

<dl>
<dd>

**return_payer_metadata:** `typing.Optional[bool]` — Whether to return payer metadata in the response
    
</dd>
</dl>

<dl>
<dd>

**return_vendor_metadata:** `typing.Optional[bool]` — Whether to return vendor metadata in the response
    
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

<details><summary><code>client.entity_group.invoice.<a href="src/mercoa/entity_group/invoice/client.py">metrics</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get invoice metrics for an entity group with the given filters. Invoices will be grouped by currency. If none of excludePayables, excludeReceivables, payerId, vendorId, or invoiceId status filters are provided, excludeReceivables will be set to true.
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

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity_group.invoice.metrics(
    entity_group_id="entg_8545a84e-a45f-41bf-bdf1-33b42a55812c",
    return_by_date="CREATION_DATE",
    exclude_receivables=True,
    start_date=datetime.datetime.fromisoformat(
        "2021-01-01 00:00:00+00:00",
    ),
    end_date=datetime.datetime.fromisoformat(
        "2021-01-31 23:59:59.999000+00:00",
    ),
    currency="USD",
    status="NEW",
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

**search:** `typing.Optional[str]` — Find invoices by vendor name, invoice number, check number, or amount. Partial matches are supported.
    
</dd>
</dl>

<dl>
<dd>

**exclude_payables:** `typing.Optional[bool]` — Only return invoices that are not payable by the entity. This will return only invoices that are receivable by the entity.
    
</dd>
</dl>

<dl>
<dd>

**exclude_receivables:** `typing.Optional[bool]` — Only return invoices that are not receivable by the entity. This will return only invoices that are payable by the entity.
    
</dd>
</dl>

<dl>
<dd>

**return_by_date:** `typing.Optional[InvoiceMetricsPerDateGroupBy]` — Return invoice metrics grouped by date.
    
</dd>
</dl>

<dl>
<dd>

**return_by_date_frequency:** `typing.Optional[InvoiceMetricsPerDateFrequency]` — Return invoice metrics grouped by date. Defaults to daily.
    
</dd>
</dl>

<dl>
<dd>

**group_by:** `typing.Optional[
    typing.Union[InvoiceMetricsGroupBy, typing.Sequence[InvoiceMetricsGroupBy]]
]` — Return invoice metrics grouped by.
    
</dd>
</dl>

<dl>
<dd>

**payer_id:** `typing.Optional[typing.Union[EntityId, typing.Sequence[EntityId]]]` — Filter invoices by payer ID.
    
</dd>
</dl>

<dl>
<dd>

**vendor_id:** `typing.Optional[typing.Union[EntityId, typing.Sequence[EntityId]]]` — Filter invoices by vendor ID.
    
</dd>
</dl>

<dl>
<dd>

**approver_id:** `typing.Optional[typing.Union[EntityUserId, typing.Sequence[EntityUserId]]]` — Filter invoices by assigned approver user ID.
    
</dd>
</dl>

<dl>
<dd>

**invoice_id:** `typing.Optional[typing.Union[InvoiceId, typing.Sequence[InvoiceId]]]` — Filter invoices by invoice ID or invoice foreign ID.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[typing.Union[InvoiceStatus, typing.Sequence[InvoiceStatus]]]` — Invoice status to filter on
    
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

**currency:** `typing.Optional[typing.Union[CurrencyCode, typing.Sequence[CurrencyCode]]]` — Currency to filter on
    
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

## Entity ApprovalPolicy
<details><summary><code>client.entity.approval_policy.<a href="src/mercoa/entity/approval_policy/client.py">get_all</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve all invoice approval policies associated with an entity
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
client.entity.approval_policy.get_all(
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

<details><summary><code>client.entity.approval_policy.<a href="src/mercoa/entity/approval_policy/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create an invoice approval policy associated with an entity
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
    ApprovalPolicyRequest,
    IdentifierList_RolesList,
    Rule_Approver,
    Trigger_Amount,
    Trigger_Catchall,
    Trigger_Metadata,
    Trigger_Vendor,
)

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.approval_policy.create(
    entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
    request=ApprovalPolicyRequest(
        trigger=[
            Trigger_Amount(
                amount=100.0,
                currency="USD",
            ),
            Trigger_Vendor(
                vendor_ids=["ent_21661ac1-a2a8-4465-a6c0-64474ba8181d"],
            ),
            Trigger_Metadata(
                key="property_id",
                value=["123456", "789012"],
            ),
            Trigger_Catchall(),
        ],
        rule=Rule_Approver(
            num_approvers=2,
            identifier_list=IdentifierList_RolesList(
                value=["Admin", "Controller"]
            ),
        ),
        upstream_policy_id="root",
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

**request:** `ApprovalPolicyRequest` 
    
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

<details><summary><code>client.entity.approval_policy.<a href="src/mercoa/entity/approval_policy/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve an invoice approval policy associated with an entity
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
client.entity.approval_policy.get(
    entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
    policy_id="apvl_5ce50275-1789-42ea-bc60-bb7e6d03635c",
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

**policy_id:** `ApprovalPolicyId` 
    
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

<details><summary><code>client.entity.approval_policy.<a href="src/mercoa/entity/approval_policy/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update an invoice approval policy associated with an entity
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
    ApprovalPolicyUpdateRequest,
    IdentifierList_RolesList,
    Rule_Approver,
    Trigger_Amount,
    Trigger_Catchall,
    Trigger_Metadata,
    Trigger_Vendor,
)

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.approval_policy.update(
    entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
    policy_id="apvl_5ce50275-1789-42ea-bc60-bb7e6d03635c",
    request=ApprovalPolicyUpdateRequest(
        trigger=[
            Trigger_Amount(
                amount=100.0,
                currency="USD",
            ),
            Trigger_Vendor(
                vendor_ids=["ent_21661ac1-a2a8-4465-a6c0-64474ba8181d"],
            ),
            Trigger_Metadata(
                key="property_id",
                value=["123456", "789012"],
            ),
            Trigger_Catchall(),
        ],
        rule=Rule_Approver(
            num_approvers=2,
            identifier_list=IdentifierList_RolesList(
                value=["Admin", "Controller"]
            ),
        ),
        upstream_policy_id="root",
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

**policy_id:** `ApprovalPolicyId` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `ApprovalPolicyUpdateRequest` 
    
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

<details><summary><code>client.entity.approval_policy.<a href="src/mercoa/entity/approval_policy/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete an invoice approval policy associated with Entity. BEWARE: Any approval policy deletion will result in all associated downstream policies also being deleted.
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
client.entity.approval_policy.delete(
    entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
    policy_id="apvl_5ce50275-1789-42ea-bc60-bb7e6d03635c",
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

**policy_id:** `ApprovalPolicyId` 
    
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

<details><summary><code>client.entity.approval_policy.<a href="src/mercoa/entity/approval_policy/client.py">history</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the history of approval policy changes for an entity
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
client.entity.approval_policy.history(
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

<details><summary><code>client.entity.approval_policy.<a href="src/mercoa/entity/approval_policy/client.py">restore</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Restore approval policies from a history entry.
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
client.entity.approval_policy.restore(
    entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
    approval_policy_history_id="hist_21661ac1-a2a8-4465-a6c0-64474ba8181d",
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

**approval_policy_history_id:** `str` 
    
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

## Entity Bnpl
<details><summary><code>client.entity.bnpl.<a href="src/mercoa/entity/bnpl/client.py">get_loans</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all BNPL loans associated with an entity
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
client.entity.bnpl.get_loans(
    entity_id="ent_123",
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

**entity_id:** `str` — The ID of the entity to get loans for
    
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

## Entity Bulk
<details><summary><code>client.entity.bulk.<a href="src/mercoa/entity/bulk/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create multiple entities in bulk. This endpoint will process synchronously and return a list of entities that were created or failed to create.
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
from mercoa.commons import Address, PhoneNumber
from mercoa.entity_types import (
    BulkConnectedEntity,
    BulkEntityCreationFromObject,
    BusinessProfileRequest,
    Ein,
    EntityCreationRequest,
    ProfileRequest,
    TaxId,
)

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.bulk.create(
    request=BulkEntityCreationFromObject(
        connected_entity=BulkConnectedEntity(
            id="ent_a0f6ea94-0761-4a5e-a416-3c453cb7eced",
            link_created_as_payor=False,
            link_created_as_payee=True,
        ),
        entities=[
            EntityCreationRequest(
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

**request:** `BulkEntityCreationRequest` 
    
</dd>
</dl>

<dl>
<dd>

**emit_webhooks:** `typing.Optional[bool]` — If true, webhooks will be emitted for each entity that is created. By default, webhooks are not emitted.
    
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

<details><summary><code>client.entity.bulk.<a href="src/mercoa/entity/bulk/client.py">download</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a URL to download a bulk entity as a CSV/JSON file.
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
client.entity.bulk.download(
    format="CSV",
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

**format:** `typing.Optional[BulkDownloadFormat]` — Format of the file to download. Defaults to CSV.
    
</dd>
</dl>

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

## Entity Counterparty Bulk
<details><summary><code>client.entity.counterparty.bulk.<a href="src/mercoa/entity/counterparty/bulk/client.py">download_payees</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a URL to download payee counterparties as a CSV/JSON file. This endpoint lets you download vendors linked to the entity.
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
client.entity.counterparty.bulk.download_payees(
    entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
    format="CSV",
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

**format:** `typing.Optional[BulkDownloadFormat]` — Format of the file to download. Defaults to CSV.
    
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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.entity.counterparty.bulk.<a href="src/mercoa/entity/counterparty/bulk/client.py">download_payors</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a URL to download payor counterparties as a CSV/JSON file. This endpoint lets you download customers linked to the entity.
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
client.entity.counterparty.bulk.download_payors(
    entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
    format="CSV",
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

**format:** `typing.Optional[BulkDownloadFormat]` — Format of the file to download. Defaults to CSV.
    
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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Entity Counterparty VendorCredit
<details><summary><code>client.entity.counterparty.vendor_credit.<a href="src/mercoa/entity/counterparty/vendor_credit/client.py">get_all</a>(...)</code></summary>
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
client.entity.counterparty.vendor_credit.get_all(
    entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
    counterparty_id="ent_21661ac1-a2a8-4465-a6c0-64474ba8181d",
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

**counterparty_id:** `EntityId` — Counterparty Entity ID or Counterparty Entity ForeignID
    
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

<details><summary><code>client.entity.counterparty.vendor_credit.<a href="src/mercoa/entity/counterparty/vendor_credit/client.py">get</a>(...)</code></summary>
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
client.entity.counterparty.vendor_credit.get(
    entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
    counterparty_id="ent_21661ac1-a2a8-4465-a6c0-64474ba8181d",
    vendor_credit_id="vcr_c3f4c87d-794d-4543-9562-575cdddfc0d7",
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

**counterparty_id:** `EntityId` — Counterparty Entity ID or Counterparty Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**vendor_credit_id:** `VendorCreditId` — ID of the vendor credit to retrieve
    
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

<details><summary><code>client.entity.counterparty.vendor_credit.<a href="src/mercoa/entity/counterparty/vendor_credit/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa
from mercoa.vendor_credit_types import VendorCreditRequest

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.counterparty.vendor_credit.create(
    entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
    counterparty_id="ent_21661ac1-a2a8-4465-a6c0-64474ba8181d",
    request=VendorCreditRequest(
        total_amount=100.0,
        currency="USD",
        note="This is a note",
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

**counterparty_id:** `EntityId` — Counterparty Entity ID or Counterparty Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**request:** `VendorCreditRequest` 
    
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

<details><summary><code>client.entity.counterparty.vendor_credit.<a href="src/mercoa/entity/counterparty/vendor_credit/client.py">delete</a>(...)</code></summary>
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
client.entity.counterparty.vendor_credit.delete(
    entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
    counterparty_id="ent_21661ac1-a2a8-4465-a6c0-64474ba8181d",
    vendor_credit_id="vcr_c3f4c87d-794d-4543-9562-575cdddfc0d7",
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

**counterparty_id:** `EntityId` — Counterparty Entity ID or Counterparty Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**vendor_credit_id:** `VendorCreditId` — ID of the vendor credit to delete
    
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

<details><summary><code>client.entity.counterparty.vendor_credit.<a href="src/mercoa/entity/counterparty/vendor_credit/client.py">estimate_usage</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Estimate the usage of vendor credits on an invoice of a given amount
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
client.entity.counterparty.vendor_credit.estimate_usage(
    entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
    counterparty_id="ent_21661ac1-a2a8-4465-a6c0-64474ba8181d",
    amount=150.0,
    currency="USD",
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

**counterparty_id:** `EntityId` — Counterparty Entity ID or Counterparty Entity ForeignID
    
</dd>
</dl>

<dl>
<dd>

**amount:** `float` — The amount of the invoice to calculate vendor credit usage for.
    
</dd>
</dl>

<dl>
<dd>

**currency:** `typing.Optional[CurrencyCode]` — The currency of the invoice to calculate vendor credit usage for. Defaults to USD.
    
</dd>
</dl>

<dl>
<dd>

**excluded_invoice_ids:** `typing.Optional[typing.Sequence[InvoiceId]]` — List of invoice IDs to exclude from the calculation. If not provided or an empty list, no invoices will be excluded. This is useful for recalculating vendor credit usage on invoices that already have vendor credits applied.
    
</dd>
</dl>

<dl>
<dd>

**included_vendor_credit_ids:** `typing.Optional[typing.Sequence[VendorCreditId]]` — List of vendor credit IDs to include in the calculation. If not provided, all applicable vendor credits will be included, while an empty list will not include ANY vendor credits.  This is useful for recalculating vendor credit usage on invoices that have a fixed list of applied vendor credits (e.g. a SCHEDULED or PENDING invoice).
    
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

## Entity Customization
<details><summary><code>client.entity.customization.<a href="src/mercoa/entity/customization/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get entity customization.
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
client.entity.customization.get(
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

<details><summary><code>client.entity.customization.<a href="src/mercoa/entity/customization/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update entity customization. This lets you turn off metadata and payment methods for an entity.
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
from mercoa.customization_types import (
    FeeCustomizationDetailRequest,
    FeeCustomizationRailRequest,
    FeeCustomizationRequest,
    MetadataCustomizationRequest,
    NotificationCustomizationRequest,
    OcrCustomizationRequest,
    PaymentMethodCustomizationRequest_BankAccount,
    PaymentMethodCustomizationRequest_Check,
    PaymentMethodCustomizationRequest_Custom,
    PaymentMethodFee_Flat,
    PaymentMethodFee_Percentage,
    WorkflowCustomizationRequest,
)
from mercoa.entity_types import EntityCustomizationRequest

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.customization.update(
    entity_id="ent_a0f6ea94-0761-4a5e-a416-3c453cb7eced",
    request=EntityCustomizationRequest(
        metadata=[
            MetadataCustomizationRequest(
                key="my_custom_field",
                disabled=True,
            ),
            MetadataCustomizationRequest(
                key="my_other_field",
                disabled=False,
            ),
        ],
        payment_source=[
            PaymentMethodCustomizationRequest_BankAccount(
                disabled=True,
                default_delivery_method="ACH_SAME_DAY",
            ),
            PaymentMethodCustomizationRequest_Custom(
                schema_id="cpms_7df2974a-4069-454c-912f-7e58ebe030fb",
                disabled=True,
            ),
        ],
        backup_disbursement=[
            PaymentMethodCustomizationRequest_Check(
                disabled=True,
                default_delivery_method="MAIL",
                print_description=True,
            )
        ],
        payment_destination=[
            PaymentMethodCustomizationRequest_BankAccount(
                disabled=True,
                default_delivery_method="ACH_SAME_DAY",
            ),
            PaymentMethodCustomizationRequest_Check(
                disabled=True,
                default_delivery_method="MAIL",
                print_description=True,
            ),
        ],
        ocr=OcrCustomizationRequest(
            line_items=True,
            collapse_line_items=True,
            invoice_metadata=True,
            line_item_metadata=True,
            line_item_gl_account_id=True,
            predict_metadata=True,
            tax_and_shipping_as_line_items=True,
            split_documents=True,
        ),
        notifications=NotificationCustomizationRequest(
            assume_role="admin",
        ),
        workflow=WorkflowCustomizationRequest(
            auto_advance_invoice_status=True,
        ),
        role_permissions={"admin": ["invoice.all", "paymentMethod.all"]},
        fees=FeeCustomizationRequest(
            payable=FeeCustomizationDetailRequest(
                source=FeeCustomizationRailRequest(
                    ach_standard=PaymentMethodFee_Flat(
                        amount=2.5,
                    ),
                    ach_same_day=PaymentMethodFee_Percentage(
                        amount=2.5,
                    ),
                    check_print=PaymentMethodFee_Flat(
                        amount=2.5,
                    ),
                    check_mail=PaymentMethodFee_Flat(
                        amount=2.5,
                    ),
                    check_mail_priority=PaymentMethodFee_Flat(
                        amount=2.5,
                    ),
                    check_mail_ups_next_day=PaymentMethodFee_Flat(
                        amount=2.5,
                    ),
                ),
                destination=FeeCustomizationRailRequest(
                    ach_standard=PaymentMethodFee_Flat(
                        amount=2.5,
                    ),
                    ach_same_day=PaymentMethodFee_Percentage(
                        amount=2.5,
                    ),
                    check_print=PaymentMethodFee_Flat(
                        amount=2.5,
                    ),
                    check_mail=PaymentMethodFee_Flat(
                        amount=2.5,
                    ),
                    check_mail_priority=PaymentMethodFee_Flat(
                        amount=2.5,
                    ),
                    check_mail_ups_next_day=PaymentMethodFee_Flat(
                        amount=2.5,
                    ),
                ),
            ),
            receivable=FeeCustomizationDetailRequest(
                source=FeeCustomizationRailRequest(
                    ach_standard=PaymentMethodFee_Flat(
                        amount=2.5,
                    ),
                    ach_same_day=PaymentMethodFee_Percentage(
                        amount=2.5,
                    ),
                    check_print=PaymentMethodFee_Flat(
                        amount=2.5,
                    ),
                    check_mail=PaymentMethodFee_Flat(
                        amount=2.5,
                    ),
                    check_mail_priority=PaymentMethodFee_Flat(
                        amount=2.5,
                    ),
                    check_mail_ups_next_day=PaymentMethodFee_Flat(
                        amount=2.5,
                    ),
                ),
                destination=FeeCustomizationRailRequest(
                    ach_standard=PaymentMethodFee_Flat(
                        amount=2.5,
                    ),
                    ach_same_day=PaymentMethodFee_Percentage(
                        amount=2.5,
                    ),
                    check_print=PaymentMethodFee_Flat(
                        amount=2.5,
                    ),
                    check_mail=PaymentMethodFee_Flat(
                        amount=2.5,
                    ),
                    check_mail_priority=PaymentMethodFee_Flat(
                        amount=2.5,
                    ),
                    check_mail_ups_next_day=PaymentMethodFee_Flat(
                        amount=2.5,
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

**request:** `EntityCustomizationRequest` 
    
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

## Entity Document
<details><summary><code>client.entity.document.<a href="src/mercoa/entity/document/client.py">get_all</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get documents (1099/W9) associated with this entity
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
client.entity.document.get_all(
    entity_id="ent_26e7b5d3-a739-4b23-9ad9-6aaa085f47a9",
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

**entity_id:** `EntityId` 
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[typing.Union[DocumentType, typing.Sequence[DocumentType]]]` — Filter by document type
    
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

<details><summary><code>client.entity.document.<a href="src/mercoa/entity/document/client.py">upload</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Upload documents associated with this entity
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
client.entity.document.upload(
    entity_id="ent_26e7b5d3-a739-4b23-9ad9-6aaa085f47a9",
    document="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAgAAAAIAQMAAAD+wSzIAAAABlBMVEX///+/v7+jQ3Y5AAAADklEQVQI12P4AIX8EAgALgAD/aNpbtEAAAAASUVORK5CYII",
    type="TEN_NINETY_NINE",
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

**entity_id:** `EntityId` 
    
</dd>
</dl>

<dl>
<dd>

**document:** `str` — Base64 encoded image or PDF of document. PNG, JPG, WEBP, and PDF are supported. 10MB max.
    
</dd>
</dl>

<dl>
<dd>

**type:** `DocumentType` 
    
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

<details><summary><code>client.entity.document.<a href="src/mercoa/entity/document/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a document associated with this entity
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
client.entity.document.delete(
    entity_id="ent_26e7b5d3-a739-4b23-9ad9-6aaa085f47a9",
    document_id="doc_37e6af0a-e637-48fd-b825-d6947b38c4e2",
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

**entity_id:** `EntityId` 
    
</dd>
</dl>

<dl>
<dd>

**document_id:** `str` 
    
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

## Entity EmailTemplate
<details><summary><code>client.entity.email_template.<a href="src/mercoa/entity/email_template/client.py">get_all</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get all email templates for the entity
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
client.entity.email_template.get_all(
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

<details><summary><code>client.entity.email_template.<a href="src/mercoa/entity/email_template/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from mercoa import Mercoa
from mercoa.entity_types import EmailTemplateRequest

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.email_template.create(
    entity_id="ent_a0f6ea94-0761-4a5e-a416-3c453cb7eced",
    request=EmailTemplateRequest(
        template_type="PAYMENT",
        name="Generic Payment Email",
        subject="Action Required - Your payment is due",
        content="<h1>Your invoice has been sent.</h1>",
        is_default=True,
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

**request:** `EmailTemplateRequest` 
    
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

<details><summary><code>client.entity.email_template.<a href="src/mercoa/entity/email_template/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get entity email template
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
client.entity.email_template.get(
    entity_id="ent_a0f6ea94-0761-4a5e-a416-3c453cb7eced",
    email_template_id="emt_8545a84e-a45f-41bf-bdf1-33b42a55812c",
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

**email_template_id:** `EmailTemplateId` — Email Template ID or Email Template ForeignID
    
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

<details><summary><code>client.entity.email_template.<a href="src/mercoa/entity/email_template/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update entity email template
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
from mercoa.entity_types import EmailTemplateRequest

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.email_template.update(
    entity_id="ent_a0f6ea94-0761-4a5e-a416-3c453cb7eced",
    email_template_id="emt_8545a84e-a45f-41bf-bdf1-33b42a55812c",
    request=EmailTemplateRequest(
        template_type="PAYMENT",
        name="Generic Payment Email",
        subject="Action Required - Your payment is due",
        content="<h1>Your invoice has been sent.</h1>",
        is_default=True,
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

**email_template_id:** `EmailTemplateId` — Email Template ID or Email Template ForeignID
    
</dd>
</dl>

<dl>
<dd>

**request:** `EmailTemplateRequest` 
    
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

<details><summary><code>client.entity.email_template.<a href="src/mercoa/entity/email_template/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete entity email template. This will also remove the email template from all entities.
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
client.entity.email_template.delete(
    entity_id="entityId",
    email_template_id="emailTemplateId",
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

**email_template_id:** `EmailTemplateId` — Email Template ID or Email Template ForeignID
    
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

## Entity ExternalAccountingSystem
<details><summary><code>client.entity.external_accounting_system.<a href="src/mercoa/entity/external_accounting_system/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get the external accounting system connected to an entity
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
client.entity.external_accounting_system.get(
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

<details><summary><code>client.entity.external_accounting_system.<a href="src/mercoa/entity/external_accounting_system/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create/Link an entity to an external accounting system like Codat or Rutter. If the entity is already linked to an external accounting system, this will return the existing connection.
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
from mercoa.entity.external_accounting_system import (
    ExternalAccountingSystemCompanyCreationRequest_Rutter,
)

client = Mercoa(
    token="YOUR_TOKEN",
)
client.entity.external_accounting_system.create(
    entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
    request=ExternalAccountingSystemCompanyCreationRequest_Rutter(
        access_token="123",
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

**request:** `ExternalAccountingSystemCompanyCreationRequest` 
    
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

<details><summary><code>client.entity.external_accounting_system.<a href="src/mercoa/entity/external_accounting_system/client.py">connect</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a link to connect an entity to an external accounting system like Quickbooks or Xero
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
client.entity.external_accounting_system.connect(
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

<details><summary><code>client.entity.external_accounting_system.<a href="src/mercoa/entity/external_accounting_system/client.py">sync</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Sync an entity with an external accounting system. Will sync customers/vendors and invoices.
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
client.entity.external_accounting_system.sync(
    entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
    vendors="pull",
    bills="push",
    gl_accounts="pull",
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

**vendors:** `typing.Optional[SyncType]` — Sync vendors from external accounting system. Default is to pull vendors from external system.
    
</dd>
</dl>

<dl>
<dd>

**bills:** `typing.Optional[SyncType]` — Sync bills from external accounting system. Default is to not sync bills. Invoices that already exist in both systems will not be updated, only new invoices not present in the other system will be created.
    
</dd>
</dl>

<dl>
<dd>

**gl_accounts:** `typing.Optional[SyncType]` — Sync GL accounts from external accounting system. Default is to pull GL accounts from external system. Pushing GL accounts is not supported.
    
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

## Entity Invoice
<details><summary><code>client.entity.invoice.<a href="src/mercoa/entity/invoice/client.py">find</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get invoices for an entity with the given filters.
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
client.entity.invoice.find(
    entity_id="ent_8545a84e-a45f-41bf-bdf1-33b42a55812c",
    exclude_receivables=True,
    order_by="CREATED_AT",
    order_direction="ASC",
    limit=10,
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

**exclude_payables:** `typing.Optional[bool]` — Return only invoices that are receivable by the entity.
    
</dd>
</dl>

<dl>
<dd>

**exclude_receivables:** `typing.Optional[bool]` — Return only invoices that are payable by the entity.
    
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

**order_by:** `typing.Optional[InvoiceOrderByField]` — Field to order invoices by. Defaults to CREATED_AT.
    
</dd>
</dl>

<dl>
<dd>

**order_direction:** `typing.Optional[OrderDirection]` — Direction to order invoices by. Defaults to asc.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of invoices to return. Limit can range between 1 and 100, and the default is 10.
    
</dd>
</dl>

<dl>
<dd>

**starting_after:** `typing.Optional[InvoiceId]` — The ID of the invoice to start after. If not provided, the first page of invoices will be returned.
    
</dd>
</dl>

<dl>
<dd>

**metadata:** `typing.Optional[typing.Union[MetadataFilter, typing.Sequence[MetadataFilter]]]` — Filter invoices by metadata. Each filter will be applied as an AND condition. Duplicate keys will be ignored.
    
</dd>
</dl>

<dl>
<dd>

**line_item_metadata:** `typing.Optional[typing.Union[MetadataFilter, typing.Sequence[MetadataFilter]]]` — Filter invoices by line item metadata. Each filter will be applied as an AND condition. Duplicate keys will be ignored.
    
</dd>
</dl>

<dl>
<dd>

**line_item_gl_account_id:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filter invoices by line item GL account ID. Each filter will be applied as an OR condition. Duplicate keys will be ignored.
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` — Find invoices by vendor name, invoice number, check number, or amount. Partial matches are supported.
    
</dd>
</dl>

<dl>
<dd>

**payer_id:** `typing.Optional[typing.Union[EntityId, typing.Sequence[EntityId]]]` — Filter invoices by payer ID or payer foreign ID.
    
</dd>
</dl>

<dl>
<dd>

**vendor_id:** `typing.Optional[typing.Union[EntityId, typing.Sequence[EntityId]]]` — Filter invoices by vendor ID or vendor foreign ID.
    
</dd>
</dl>

<dl>
<dd>

**creator_user_id:** `typing.Optional[typing.Union[EntityUserId, typing.Sequence[EntityUserId]]]` — Filter invoices by the ID or foreign ID of the user that created the invoice.
    
</dd>
</dl>

<dl>
<dd>

**approver_id:** `typing.Optional[typing.Union[EntityUserId, typing.Sequence[EntityUserId]]]` — Filter invoices by assigned approver user ID.
    
</dd>
</dl>

<dl>
<dd>

**approver_action:** `typing.Optional[typing.Union[ApproverAction, typing.Sequence[ApproverAction]]]` — Filter invoices by approver action. Needs to be used with approverId. For example, if you want to find all invoices that have been approved by a specific user, you would use approverId and approverAction=APPROVE.
    
</dd>
</dl>

<dl>
<dd>

**invoice_id:** `typing.Optional[typing.Union[InvoiceId, typing.Sequence[InvoiceId]]]` — Filter invoices by invoice ID or invoice foreign ID.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[typing.Union[InvoiceStatus, typing.Sequence[InvoiceStatus]]]` — Invoice status to filter on.
    
</dd>
</dl>

<dl>
<dd>

**payment_type:** `typing.Optional[typing.Sequence[PaymentType]]` — Filter invoices by payment type.
    
</dd>
</dl>

<dl>
<dd>

**return_payer_metadata:** `typing.Optional[bool]` — Whether to return payer metadata in the response
    
</dd>
</dl>

<dl>
<dd>

**return_vendor_metadata:** `typing.Optional[bool]` — Whether to return vendor metadata in the response
    
</dd>
</dl>

<dl>
<dd>

**return_payment_timing:** `typing.Optional[bool]` — Whether to return payment timing in the response
    
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

<details><summary><code>client.entity.invoice.<a href="src/mercoa/entity/invoice/client.py">metrics</a>(...)</code></summary>
