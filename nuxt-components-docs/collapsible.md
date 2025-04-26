<!-- source: https://ui.nuxt.com/components/collapsible --> # Collapsible

[Collapsible](https://reka-
ui.com/docs/components/collapsible)[GitHub](https://github.com/nuxt/ui/tree/v3/src/runtime/components/Collapsible.vue)

A collapsible element to toggle visibility of its content.

## Usage

Use a [Button](/components/button) or any other component in the default slot
of the Collapsible.

Then, use the `#content` slot to add the content displayed when the
Collapsible is open.

    
    
    <template>
      <UCollapsible class="flex flex-col gap-2 w-48">
        <UButton
          label="Open"
          color="neutral"
          variant="subtle"
          trailing-icon="i-lucide-chevron-down"
          block
        />
    
        <template #content>
          <Placeholder class="h-48" />
        </template>
      </UCollapsible>
    </template>
    

### Unmount

Use the `unmount-on-hide` prop to prevent the content from being unmounted
when the Collapsible is collapsed. Defaults to `true`.

unmountOnHide

false

    
    
    <template>
      <UCollapsible :unmount-on-hide="false" class="flex flex-col gap-2 w-48">
        <UButton
          label="Open"
          color="neutral"
          variant="subtle"
          trailing-icon="i-lucide-chevron-down"
          block
        />
    
        <template #content>
          <Placeholder class="h-48" />
        </template>
      </UCollapsible>
    </template>
    

You can inspect the DOM to see the content being rendered.

### Disabled

Use the `disabled` prop to disable the Collapsible.

disabled

true

    
    
    <template>
      <UCollapsible class="flex flex-col gap-2 w-48" disabled>
        <UButton
          label="Open"
          color="neutral"
          variant="subtle"
          trailing-icon="i-lucide-chevron-down"
          block
        />
    
        <template #content>
          <Placeholder class="h-48" />
        </template>
      </UCollapsible>
    </template>
    

## Examples

### Control open state

You can control the open state by using the `default-open` prop or the
`v-model:open` directive.

Open

    
    
    <script setup lang="ts">
    const open = ref(true)
    
    defineShortcuts({
      o: () => open.value = !open.value
    })
    </script>
    
    <template>
      <UCollapsible v-model:open="open" class="flex flex-col gap-2 w-48">
        <UButton
          label="Open"
          color="neutral"
          variant="subtle"
          trailing-icon="i-lucide-chevron-down"
          block
        />
    
        <template #content>
          <Placeholder class="h-48" />
        </template>
      </UCollapsible>
    </template>
    

In this example, leveraging [`defineShortcuts`](/composables/define-
shortcuts), you can toggle the Collapsible by pressing `O`.

This allows you to move the trigger outside of the Collapsible or remove it
entirely.

### With rotating icon

Here is an example with a rotating icon in the Button that indicates the open
state of the Collapsible.

Open

    
    
    <template>
      <UCollapsible class="flex flex-col gap-2 w-48">
        <UButton
          class="group"
          label="Open"
          color="neutral"
          variant="subtle"
          trailing-icon="i-lucide-chevron-down"
          :ui="{
            trailingIcon: 'group-data-[state=open]:rotate-180 transition-transform duration-200'
          }"
          block
        />
    
        <template #content>
          <Placeholder class="h-48" />
        </template>
      </UCollapsible>
    </template>
    

## API

### Props

Prop |  Default |  Type   
---|---|---  
`as`| `'div'`| `any`The element or component this component should render as.  
`disabled`| | `boolean`When `true`, prevents the user from interacting with the collapsible.  
`defaultOpen`| | `boolean`The open state of the collapsible when it is initially rendered.   
Use when you do not need to control its open state.  
`open`| | `boolean`The controlled open state of the collapsible. Can be binded with `v-model`.  
`unmountOnHide`| `true`| `boolean`When `true`, the element will be unmounted
on closed state.  
`ui`| | ` { root?: ClassNameValue; content?: ClassNameValue; }`  
  
### Slots

Slot |  Type   
---|---  
`default`| `{ open: boolean; }`  
`content`| `{}`  
  
### Emits

Event |  Type   
---|---  
`update:open`| `[value: boolean]`  
  
## Theme

app.config.ts

    
    
    export default defineAppConfig({
      ui: {
        collapsible: {
          slots: {
            root: '',
            content: 'data-[state=open]:animate-[collapsible-down_200ms_ease-out] data-[state=closed]:animate-[collapsible-up_200ms_ease-out] overflow-hidden'
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
            collapsible: {
              slots: {
                root: '',
                content: 'data-[state=open]:animate-[collapsible-down_200ms_ease-out] data-[state=closed]:animate-[collapsible-up_200ms_ease-out] overflow-hidden'
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
            collapsible: {
              slots: {
                root: '',
                content: 'data-[state=open]:animate-[collapsible-down_200ms_ease-out] data-[state=closed]:animate-[collapsible-up_200ms_ease-out] overflow-hidden'
              }
            }
          }
        })
      ]
    })
    

Expand code

[ChipAn indicator of a numeric value or a
state.](/components/chip)[ColorPickerA component to select a
color.](/components/color-picker)

