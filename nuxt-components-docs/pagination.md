<!-- source: https://ui.nuxt.com/components/pagination --> # Pagination

[Pagination](https://reka-
ui.com/docs/components/pagination)[GitHub](https://github.com/nuxt/ui/tree/v3/src/runtime/components/Pagination.vue)

A list of buttons or links to navigate through pages.

## Usage

Use the `default-page` prop or the `v-model:page` directive to control the
current page.

The Pagination component uses some [`Button`](/components/button) to display
the pages, use `color`, `variant` and `size` props to style them.

### Total

Use the `total` prop to set the total number of items in the list.

page

total

    
    
    <script setup lang="ts">
    const page = ref(5)
    </script>
    
    <template>
      <UPagination v-model:page="page" :total="100" />
    </template>
    

### Items Per Page

Use the `items-per-page` prop to set the number of items per page. Defaults to
`10`.

itemsPerPage

total

    
    
    <script setup lang="ts">
    const page = ref(5)
    </script>
    
    <template>
      <UPagination v-model:page="page" :items-per-page="20" :total="100" />
    </template>
    

### Sibling Count

Use the `sibling-count` prop to set the number of siblings to show. Defaults
to `2`.

siblingCount

    
    
    <script setup lang="ts">
    const page = ref(5)
    </script>
    
    <template>
      <UPagination v-model:page="page" :sibling-count="1" :total="100" />
    </template>
    

### Show Edges

Use the `show-edges` prop to always show the ellipsis, first and last pages.
Defaults to `false`.

showEdges

true

siblingCount

    
    
    <script setup lang="ts">
    const page = ref(5)
    </script>
    
    <template>
      <UPagination v-model:page="page" show-edges :sibling-count="1" :total="100" />
    </template>
    

### Show Controls

Use the `show-controls` prop to show the first, prev, next and last buttons.
Defaults to `true`.

showControls

false

showEdges

true

    
    
    <script setup lang="ts">
    const page = ref(5)
    </script>
    
    <template>
      <UPagination v-model:page="page" :show-controls="false" show-edges :total="100" />
    </template>
    

### Color

Use the `color` prop to set the color of the inactive controls. Defaults to
`neutral`.

color

primary

    
    
    <script setup lang="ts">
    const page = ref(5)
    </script>
    
    <template>
      <UPagination v-model:page="page" color="primary" :total="100" />
    </template>
    

### Variant

Use the `variant` prop to set the variant of the inactive controls. Defaults
to `outline`.

color

neutral

variant

subtle

    
    
    <script setup lang="ts">
    const page = ref(5)
    </script>
    
    <template>
      <UPagination v-model:page="page" color="neutral" variant="subtle" :total="100" />
    </template>
    

### Active Color

Use the `active-color` prop to set the color of the active control. Defaults
to `primary`.

activeColor

neutral

    
    
    <script setup lang="ts">
    const page = ref(5)
    </script>
    
    <template>
      <UPagination v-model:page="page" active-color="neutral" :total="100" />
    </template>
    

### Active Variant

Use the `active-variant` prop to set the variant of the active control.
Defaults to `solid`.

activeColor

primary

activeVariant

subtle

    
    
    <script setup lang="ts">
    const page = ref(5)
    </script>
    
    <template>
      <UPagination v-model:page="page" active-color="primary" active-variant="subtle" :total="100" />
    </template>
    

### Size

Use the `size` prop to set the size of the controls. Defaults to `md`.

size

xl

    
    
    <script setup lang="ts">
    const page = ref(5)
    </script>
    
    <template>
      <UPagination v-model:page="page" size="xl" :total="100" />
    </template>
    

### Disabled

Use the `disabled` prop to disable the pagination controls.

disabled

true

    
    
    <script setup lang="ts">
    const page = ref(5)
    </script>
    
    <template>
      <UPagination v-model:page="page" :total="100" disabled />
    </template>
    

## Examples

### With links

Use the `to` prop to transform buttons into links. Pass a function that
receives the page number and returns a route destination.

    
    
    <script setup lang="ts">
    const page = ref(5)
    
    function to(page: number) {
      return {
        query: {
          page
        },
        hash: '#with-links'
      }
    }
    </script>
    
    <template>
      <UPagination v-model:page="page" :total="100" :to="to" :sibling-count="1" show-edges />
    </template>
    

In this example we're adding the `#with-links` hash to avoid going to the top
of the page.

## API

### Props

Prop |  Default |  Type   
---|---|---  
`as`| `'div'`| `any`The element or component this component should render as.  
`firstIcon`| `appConfig.ui.icons.chevronDoubleLeft`| ` string`The icon to use
for the first page control.  
`prevIcon`| `appConfig.ui.icons.chevronLeft`| ` string`The icon to use for the
previous page control.  
`nextIcon`| `appConfig.ui.icons.chevronRight`| ` string`The icon to use for
the next page control.  
`lastIcon`| `appConfig.ui.icons.chevronDoubleRight`| ` string`The icon to use
for the last page control.  
`ellipsisIcon`| `appConfig.ui.icons.ellipsis`| ` string`The icon to use for
the ellipsis control.  
`color`| `'neutral'`| ` "error" | "primary" | "secondary" | "success" | "info" | "warning" | "neutral"`The color of the pagination controls.  
`variant`| `'outline'`| ` "link" | "solid" | "outline" | "soft" | "subtle" | "ghost"`The variant of the pagination controls.  
`activeColor`| `'primary'`| ` "error" | "primary" | "secondary" | "success" | "info" | "warning" | "neutral"`The color of the active pagination control.  
`activeVariant`| `'solid'`| ` "link" | "solid" | "outline" | "soft" | "subtle" | "ghost"`The variant of the active pagination control.  
`showControls`| `true`| `boolean`Whether to show the first, previous, next,
and last controls.  
`size`| `'md'`| ` "sm" | "md" | "xs" | "lg" | "xl"`  
`to`| | `(page: number): string | RouteLocationAsRelativeGeneric | RouteLocationAsPathGeneric`A function to render page controls as links.  
`disabled`| | `boolean`When `true`, prevents the user from interacting with item  
`page`| | ` number`The controlled value of the current page. Can be binded as `v-model:page`.  
`defaultPage`| | ` number`The value of the page that should be active when initially rendered.Use when you do not need to control the value state.  
`itemsPerPage`| `10`| ` number`Number of items per page  
`showEdges`| `false`| `boolean`When `true`, always show first page, last page,
and ellipsis  
`siblingCount`| `2`| ` number`Number of sibling should be shown around the
current page  
`total`| `0`| ` number`Number of items in your list  
`ui`| | ` { root?: ClassNameValue; list?: ClassNameValue; ellipsis?: ClassNameValue; label?: ClassNameValue; first?: ClassNameValue; prev?: ClassNameValue; item?: ClassNameValue; next?: ClassNameValue; last?: ClassNameValue; }`  
  
### Slots

Slot |  Type   
---|---  
`first`| `{}`  
`prev`| `{}`  
`next`| `{}`  
`last`| `{}`  
`ellipsis`| `{}`  
`item`| `{ page: number; pageCount: number; item: { type: "ellipsis"; } | { type: "page"; value: number; }; index: number; }`  
  
### Emits

Event |  Type   
---|---  
`update:page`| `[value: number]`  
  
## Theme

app.config.ts

    
    
    export default defineAppConfig({
      ui: {
        pagination: {
          slots: {
            root: '',
            list: 'flex items-center gap-1',
            ellipsis: 'pointer-events-none',
            label: 'min-w-5 text-center',
            first: '',
            prev: '',
            item: '',
            next: '',
            last: ''
          }
        }
      }
    })
    

Expand code

vite.config.ts

    
    
    import { defineConfig } from 'vite'
    import vue from '@vitejs/plugin-vue'
    import ui from '@nuxt/ui/vite'
    
    export default defineConfig({
      plugins: [
        vue(),
        ui({
          ui: {
            pagination: {
              slots: {
                root: '',
                list: 'flex items-center gap-1',
                ellipsis: 'pointer-events-none',
                label: 'min-w-5 text-center',
                first: '',
                prev: '',
                item: '',
                next: '',
                last: ''
              }
            }
          }
        })
      ]
    })
    

Expand code

vite.config.ts

    
    
    import { defineConfig } from 'vite'
    import vue from '@vitejs/plugin-vue'
    import uiPro from '@nuxt/ui-pro/vite'
    
    export default defineConfig({
      plugins: [
        vue(),
        uiPro({
          ui: {
            pagination: {
              slots: {
                root: '',
                list: 'flex items-center gap-1',
                ellipsis: 'pointer-events-none',
                label: 'min-w-5 text-center',
                first: '',
                prev: '',
                item: '',
                next: '',
                last: ''
              }
            }
          }
        })
      ]
    })
    

Expand code

[NavigationMenuA list of links that can be displayed horizontally or
vertically.](/components/navigation-menu)[PinInputAn input element to enter a
pin.](/components/pin-input)

